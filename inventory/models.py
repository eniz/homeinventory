# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Building(models.Model):
  name = models.CharField(max_length=10)

  def __str__(self):
      return self.name


class Apartment(models.Model):
  number = models.CharField(max_length=50)
  building = models.ForeignKey(Building)

  def __str__(self):
      return str(self.number) + '-' + self.building.name


class Room(models.Model):
  name = models.CharField(max_length=50)
  apartment = models.ForeignKey(Apartment)

  def __str__(self):
      return self.apartment.number + '-' + str(self.name)


class Product(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  room = models.ForeignKey(Room)

  def __str__(self):
      return str(self.name) + '-' + self.room.name
