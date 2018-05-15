from django.urls import path


from . import views

urlpatterns = [
    # ex: /car/
    path('', views.car_index, name='car_index'),
    # ex /car/2
    path('<int:car_id>/', views.car_details, name='car_details'),
    # ex /car/add
    path('add/', views.add_car, name='add_car'),


]