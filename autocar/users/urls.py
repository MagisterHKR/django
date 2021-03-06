from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views

urlpatterns = [
# ex: profil/
    path('', login_required(views.profil) , name='profil'),
# ex: profil/edit/1
    path('edit/<int:user_id>',login_required(views.edit_profile), name='edit_profil'),
# ex: profil/32
    path('<int:user_id>', login_required(views.profil_id) , name='profil_id'),
# ex: profil/list
    path('list/', login_required(views.list_profil), name='list_profil'),
    # ex: profil/login
    path('login/', views.login, name='login'),
# ex: profil/logout
    path('logout/', views.logout, name='logout'),
# ex: profil/register
    path('register/',views.registration, name='register'),
# ex: profil/register/succes
    path('register/succes',views.reg_succ, name='register_success'),
# ex: profil/change_password
    path('change_password/', login_required(views.password_chnge), name='password_change'),
# ex: profil/password
    path('password/', login_required(views.create_password), name='create'),

]