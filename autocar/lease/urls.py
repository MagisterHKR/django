from django.urls import path
from django.contrib.auth import views as auth_views
from lease.models import Raport
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [

    path('raports/', login_required(views.RaportsListView.as_view()), name='raport_list'),
    path('<int:car_id>',views.CreateRaport, name='raport_create'),
    path('success/', views.success, name='success'),
    path('raports/detail/<int:raport_id>', login_required(views.RaportDetail), name='raport_detail'),
    path('raports/accept/<int:raport_id>', login_required(views.RaportAccept), name='raport_accept'),
    path('raports/done/<int:raport_id>', login_required(views.CarAcctept), name='raport_car_accept'),
    path('raports/reject/<int:raport_id>', login_required(views.CarReject), name='raport_car_reject'),
    path('raports/end/<int:raport_id>', login_required(views.CarDone), name='raport_car_done'),
    path('raports/delete/<int:raport_id>', login_required(views.ReportDelete), name='raport_delete'),

]