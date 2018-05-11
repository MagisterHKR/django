from django.urls import path

from . import views

urlpatterns = [
    # ex: /car/
    path('', views.index, name='index'),
    # ex /car/2
    path('<int:car_id>/', views.details, name='details'),
    # ex /car/add
    path('add/', views.add_car, name='add_car'),
    path('test/', views.add_ca, name='add_ca'),
]