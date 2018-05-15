from django.urls import path

from . import views

urlpatterns = [
    path('', views.lease_index, name='lease_index'),
    #path('', views.lease_details, name='lease_details'),
]