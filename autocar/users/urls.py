from django.urls import path

from . import views

urlpatterns = [
    # ex: /car/
    path('', views.profil, index='profil'),
    # ex /car/2


]