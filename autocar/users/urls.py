from django.urls import path

from . import views

urlpatterns = [

    path('', views.profil , name='profil'),
    path('list/', views.list_profil, name='list_profil')
    #path('<int:user_id>/', views.list_profil, name='list_profil')


]