import pickle
import sys

import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics
import json
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from fa.model import FinAdvisorModel
import numpy as np
import os
from django.conf import settings

from .models import Okved, Industry, Region
from .serializers import OkvedSerializer, IndustrySerializer, RegionSerializer


# MODEL_PARAMS = dict(
#     # n_estimators=2000,
#     # learning_rate=0.01,
#     # # reg_alpha=1,
#     # reg_lambda=1,
#     # num_leaves=40,
#     # min_child_samples=5,
#     # importance_type="gain",
#     # n_jobs=1,
#     random_state=42,
#     silent=False,
#     class_weight='balanced',
#     max_depth=2
# )
# num_features = ['inv_sum', 'inv_ind_1500', 'inv_ind_1200', 'inv_ind_1300', 'inv_ind_1400']
# ohe_features = ['okved', 'region']
# train_df = pd.read_csv(os.path.join(settings.BASE_DIR, 'train.csv'))
# train_df['okved'] = train_df['okved'].apply(lambda x: x.strip())
# train_df['region'] = train_df['region'].apply(lambda x: str(x).strip())
# fa_model = FinAdvisorModel(num_features=num_features, ohe_features=ohe_features, model_params=MODEL_PARAMS)
# fa_model.fit(train_df, train_df['target'])
# fa_model.save(os.path.join(settings.BASE_DIR, 'fa_model.pkl'))

def get_all_okveds(request):
    queryset = Okved.objects.all()
    serializer = OkvedSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def get_okveds_by_industry(request, industry):
    queryset = Okved.objects.all().filter(industry_code=industry)
    serializer = OkvedSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def get_all_industries(request):
    queryset = Industry.objects.all()
    serializer = IndustrySerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def get_all_regions(request):
    queryset = Region.objects.all()
    serializer = RegionSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def get_prediction(request):
    sum = request.GET.get('sum')
    okved = request.GET.get('okved')
    region = request.GET.get('region')

    file_ = os.path.join(settings.BASE_DIR, 'fa_model.pkl')
    fa_model = FinAdvisorModel.load(file_)
    prediction = fa_model.predict_one(np.log(int(sum) / 1000), okved, region)

    pred_dict = {
        'noprofit': prediction[0][0],
        'year_0': prediction[0][1],
        'year_1': prediction[0][2],
        'year_2': prediction[0][3],
        'year_3': prediction[0][4],
        'year_4': prediction[0][5],
        'year_5': prediction[0][6],
    }

    return JsonResponse(pred_dict, safe=False, json_dumps_params={'ensure_ascii': False})


def index(request):
    return render(request, 'index.html')
