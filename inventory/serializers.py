from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'price',)
        model = models.Product
        order_by = 'name'


class RoomSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        fields = ('name', 'products')
        model = models.Room
        order_by = 'name'


class ApartmentSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        fields = ('number', 'rooms')
        model = models.Apartment
        order_by = 'number'


class BuildingSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)

    class Meta:
        fields = ('name', 'apartments')
        model = models.Building
        order_by = 'name'
