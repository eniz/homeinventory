# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Building
from django.test import TestCase


class BuildingTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Building.objects.create(name='X Apartmani')
        Building.objects.create(name='Y Apartmani')

    def test_building_name(self):
        x_apt = Building.objects.get(name='X Apartmani')
        y_apt = Building.objects.get(name='Y Apartmani')
        self.assertEqual(x_apt.get_name('X Apartmani'))
        self.assertEqual(y_apt.get_name('Y Apartmani'))