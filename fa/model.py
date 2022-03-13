#!/usr/bin/env python3

import numpy as np
import pandas as pd
import pickle

from sklearn.exceptions import NotFittedError
from typing import List
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from lightgbm import LGBMClassifier

RANDOM_SEED = 42


class FinAdvisorModel():
    def __init__(self, num_features: List[str],
                 ohe_features=None,
                 model_params=None):
        if model_params is None:
            model_params = {'random_state': RANDOM_SEED}
        if ohe_features is None:
            ohe_features = []

        self.num_features = num_features
        self.ohe_features = ohe_features

        self.__is_fitted = False

        self.preprocessor = ColumnTransformer(transformers=[
            ('num', StandardScaler(), self.num_features),
            ('ohe', OneHotEncoder(handle_unknown='ignore'), self.ohe_features),
        ])

        self.model = LGBMClassifier(**model_params)

        self.pipeline = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('model', self.model)])

        self._is_fitted = False

    def fit(self, X: pd.DataFrame, y: pd.Series):
        """Обучение модели.

        :param X: pd.DataFrame с записями по организациям
        :param y: pd.Series - сроки окупаемости (-1 - не окупиться, 0..5 лет до окупаемости)
        """
        self.pipeline.fit(X[self.num_features + self.ohe_features], y)
        self.__is_fitted = True

    def predict(self, X: pd.DataFrame) -> np.array:
        """Предсказание модели
        :param X: pd.DataFrame
        :return: np.array, сроки окупаемости (-1 - не окупиться, 0..5 лет до окупаемости)
        """
        if self.__is_fitted:
            return self.pipeline.predict(X[self.num_features + self.ohe_features])
        else:
            raise NotFittedError(
                "This {} instance is not fitted yet! Call 'fit' with appropriate arguments before predict".format(
                    type(self).__name__
                )
            )

    def predict_proba(self, X: pd.DataFrame) -> np.array:
        """Предсказание модели
        :param X: pd.DataFrame
        :return: np.array, вероятность сроков окупаемости ([0] - не окупиться, [1...5] - годы от 0 до 4)
        """
        if self.__is_fitted:
            return self.pipeline.predict_proba(X[self.num_features + self.ohe_features])
        else:
            raise NotFittedError(
                "This {} instance is not fitted yet! Call 'fit' with appropriate arguments before predict".format(
                    type(self).__name__
                )
            )

    def predict_one(self, inv_sum: int, okved: str, region: str, **args: None) -> np.array:
        data_dict = {
            'inv_sum': inv_sum,
            'okved': okved,
            'region': region
        }

        if args is not None:
            data_dict = dict(data_dict, **args)

        for feature in self.num_features + self.ohe_features:
            if feature not in data_dict:
                data_dict[feature] = 0

        data = pd.DataFrame([data_dict.values()], columns=data_dict.keys())

        return self.predict_proba(data)

    def save(self, path: str):
        """Сериализует модель в pickle.
        :param path: str, путь до файла
        """
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load(self, path: str):
        """Сериализует модель в pickle.
        :param path: str, путь до файла
        :return: Модель
        """
        with open(path, "rb") as f:
            model = pickle.load(f)
        return model
