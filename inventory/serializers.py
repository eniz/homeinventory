from rest_framework import serializers
from . import models


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name',)
        model = models.Building


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'number',)
        model = models.Apartment


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name',)
        model = models.Room


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'price',)
        model = models.Product