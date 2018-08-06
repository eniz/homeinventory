from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'price',)
        model = models.Product


class RoomSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        fields = ('id', 'name', 'products')
        model = models.Room


class ApartmentSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True)

    class Meta:
        fields = ('id', 'number', 'rooms')
        model = models.Apartment


class BuildingSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True)

    class Meta:
        fields = ('id', 'name', 'apartments')
        model = models.Building
