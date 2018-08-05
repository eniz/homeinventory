# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .models import Building, Apartment, Room, Product
from . import serializers


class BuildingListCreate(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = serializers.BuildingSerializer


class BuildingDetail(generics.RetrieveUpdateAPIView):
    queryset = Building.objects.all()
    serializer_class = serializers.BuildingSerializer


class ApartmentListCreate(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer


class ApartmentDetail(generics.RetrieveUpdateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer


class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer


class RoomDetail(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
