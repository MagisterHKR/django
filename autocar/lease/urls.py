from django.urls import path

from lease.models import Raport
from . import views


urlpatterns = [

    path('raports/', views.RaportsListView.as_view(), name='raport_list'),
    path('<int:car_id>',views.CreateRaport, name='raport_create'),
    path('success/', views.success, name='success'),
]