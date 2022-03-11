from django.http import HttpResponse, JsonResponse
from rest_framework import generics
import json
from django.core import serializers
from rest_framework.renderers import JSONRenderer

from .models import Okved, Industry, Region
from .serializers import OkvedSerializer, IndustrySerializer, RegionSerializer


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
