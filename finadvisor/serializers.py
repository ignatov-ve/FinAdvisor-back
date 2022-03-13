from rest_framework import serializers

from .models import Okved, Industry, Region


class OkvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Okved
        fields = ('okved', 'name', 'industry_code')


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('code', 'name')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('code', 'name')
