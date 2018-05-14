from django.urls import path
from . import views
urlpatterns = [
    # ex /car/add
    path('add/<int:car_id>', views.add_hire, name='add_hire'),

]