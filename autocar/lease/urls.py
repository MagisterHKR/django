from django.urls import path

from lease.models import Raport
from . import views


urlpatterns = [

    path('raports/', views.RaportsListView.as_view(), name='raport_list'),
    path('<int:car_id>',views.CreateRaport, name='raport_create'),
    path('success/', views.success, name='success'),
    path('raports/detail/<int:raport_id>', views.RaportDetail, name='raport_detail'),
    path('raports/accept/<int:raport_id>', views.RaportAccept, name='raport_accept'),
    path('raports/done/<int:raport_id>', views.CarAcctept, name='raport_car_accept'),
    path('raports/reject/<int:raport_id>', views.CarReject, name='raport_car_reject'),
]