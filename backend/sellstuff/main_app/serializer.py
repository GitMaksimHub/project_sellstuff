import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import db_api_test



class db_api_test_serializer(serializers.ModelSerializer):
    class Meta:
        model = db_api_test
        fields = '__all__'
