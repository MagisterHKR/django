from django.urls import path


from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # ex: /
    path('', views.CarListView.as_view(), name='car_list'),
    # ex: /2
    path('<int:car_id>/', views.CarDetailView.as_view(), name='car_detail'),
    # ex: /create
    path('create/',login_required(views.CarCreateView.as_view()), name='car_create'),
    # ex: 2/update
    path('<int:car_id>/<slug:slug>', login_required(views.CarUpdateView.as_view()), name='car_update'),




]