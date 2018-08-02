from django.conf.urls import url

from . import views

urlpatterns = [
    url('building/', views.BuildingListCreate.as_view()),
]