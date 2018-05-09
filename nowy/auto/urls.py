from django.urls import path

from . import views

urlpatterns = [
    # ex: /auto/
    path('', views.index, name='index'),
    # ex /auto/2
    path('<int:auto_id>/', views.details, name='details'),


]