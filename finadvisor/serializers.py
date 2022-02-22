from rest_framework import serializers

from .models import Okved


class OkvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Okved
        fields = ('okved', 'name')
