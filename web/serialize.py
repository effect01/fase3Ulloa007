from .models import GenBook
from rest_framework import serializers


class GenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GenBook
        fields = '__all__'

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GenBook
        fields = '__all__'