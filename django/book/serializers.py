from rest_framework import serializers
from .models import *


class PublishingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishingHouse
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    publish_house = PublishingHouseSerializer

    class Meta:
        model = Book
        fields = '__all__'