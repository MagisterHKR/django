from django.urls import path

<<<<<<< HEAD

from . import views
from django.contrib.auth.decorators import login_required
=======
from .models import Car
from . import views
from django.contrib.auth.decorators import login_required, permission_required
>>>>>>> 7760546998b33c19420eee8164288752cfa3a93d

urlpatterns = [
    # ex: /
    path('', views.CarListView.as_view(), name='car_list'),
    # ex: /2
    path('<int:car_id>/', views.CarDetailView.as_view(), name='car_detail'),
<<<<<<< HEAD
    # ex: /create
    path('create/',login_required(views.CarCreateView.as_view()), name='car_create'),
    # ex: 2/update
=======
    # ex /car/add
    path('create/',login_required(views.CarCreateView.as_view()), name='car_create'),
>>>>>>> 7760546998b33c19420eee8164288752cfa3a93d
    path('<int:car_id>/<slug:slug>', login_required(views.CarUpdateView.as_view()), name='car_update'),




]