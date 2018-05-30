from django.urls import path

from .models import Car
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    # ex: /car/
    path('', views.CarListView.as_view(), name='car_list'),
    # ex /car/2
    path('<int:car_id>/', views.CarDetailView.as_view(), name='car_detail'),
    # ex /car/add
    path('create/',login_required(views.CarCreateView.as_view()), name='car_create'),
    path('<int:car_id>/<slug:slug>', login_required(views.CarUpdateView.as_view()), name='car_update'),




]