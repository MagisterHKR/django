from django.urls import path

from .models import Car
from . import views


urlpatterns = [
    # ex: /car/
    path('', views.CarListView.as_view(), name='car_list'),
    # ex /car/2
    path('<int:car_id>/', views.CarDetailView.as_view(), name='car_detail'),
    # ex /car/add
    path('create/', views.CarCreateView.as_view(), name='car_create'),
    path('<int:car_id>/<slug:slug>', views.CarUpdateView.as_view(), name='car_update'),




]