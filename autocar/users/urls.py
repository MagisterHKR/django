from django.urls import path

from . import views

urlpatterns = [

    path('', views.profil , name='profil'),
    path('<int:user_id>', views.profil_id , name='profil_id'),
    path('list/', views.list_profil, name='list_profil'),
    #path('<int:user_id>/', views.list_profil, name='list_profil'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('logged/', views.logged, name='legged'),
    path('register/',views.registration, name='register'),
    path('register/succes',views.reg_succ, name='register_success'),



]