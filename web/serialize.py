from .models import GenBook
from rest_framework import serializers


class GenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenBook
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenBook
        fields = '__all__'