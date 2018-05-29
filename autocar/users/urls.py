from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views

urlpatterns = [

    path('', login_required(views.profil) , name='profil'),
    path('edit/<int:user_id>',login_required(views.edit_profile), name='edit_profil'),
    path('<int:user_id>', login_required(views.profil_id) , name='profil_id'),
    path('list/', login_required(views.list_profil), name='list_profil'),
    #path('<int:user_id>/', views.list_profil, name='list_profil'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('logged/', views.logged, name='legged'),
    path('register/',views.registration, name='register'),
    path('register/succes',views.reg_succ, name='register_success'),
    path('change_password/', login_required(views.password_chnge), name='password_change'),
    path('password/', login_required(views.create_password), name='create'),



]