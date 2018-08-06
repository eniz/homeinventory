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


class ApartmentList(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer

    def get_queryset(self):
        queryset = super(ApartmentList, self).get_queryset()
        building_id = self.kwargs['pk']
        return queryset.filter(building_id=building_id)


class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer


class RoomDetail(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer


class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer

    def get_queryset(self):
        queryset = super(RoomList, self).get_queryset()
        apartment_id = self.kwargs['pk']
        return queryset.filter(apartment_id=apartment_id)


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
