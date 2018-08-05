from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # url('', TemplateView.as_view(template_name='index.html')),
    url(r'^buildings/$', views.BuildingListCreate.as_view()),
    url(r'^buildings/(?P<pk>[0-9]+)/$', views.BuildingDetail.as_view()),
    url(r'^buildings/(?P<pk>[0-9]+)/apartments$', views.ApartmentList.as_view()),
    url(r'^apartments/$', views.ApartmentListCreate.as_view()),
    url(r'^apartments/(?P<pk>[0-9]+)/$', views.ApartmentDetail.as_view()),
    url(r'^apartments/(?P<pk>[0-9]+)/rooms$', views.RoomList.as_view()),
    url(r'^rooms/$', views.RoomListCreate.as_view()),
    url(r'^rooms/(?P<pk>[0-9]+)/$', views.RoomDetail.as_view()),
    url(r'^products/$', views.ProductListCreate.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
]