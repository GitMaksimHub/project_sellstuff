from rest_framework import serializers
from .models import db_api_test

class db_api_test_serializer(serializers.ModelSerializer):
    class Meta:
        model = db_api_test
        fields = ["title", "description"]