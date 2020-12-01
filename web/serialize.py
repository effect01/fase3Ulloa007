from .models import Author, GenBook
from rest_framework import serializers


class GenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenBook
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'