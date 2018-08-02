# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Building)
admin.site.register(models.Apartment)
admin.site.register(models.Room)
admin.site.register(models.Product)