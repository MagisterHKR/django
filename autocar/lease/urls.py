from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # ex: lease/raports
    path('raports/', login_required(views.RaportsListView.as_view()), name='raport_list'),
    # ex: lease/65
    path('<int:car_id>',views.CreateRaport, name='raport_create'),
    # ex: lease/succes
    path('success/', views.success, name='success'),
    # ex: lease/raports/detail/32
    path('raports/detail/<int:raport_id>', login_required(views.RaportDetail), name='raport_detail'),
    # ex: lease/raports/accept/32
    path('raports/accept/<int:raport_id>', login_required(views.RaportAccept), name='raport_accept'),
# ex: lease/raports/done/32
    path('raports/done/<int:raport_id>', login_required(views.CarAcctept), name='raport_car_accept'),
# ex: lease/raports/reject/32
    path('raports/reject/<int:raport_id>', login_required(views.CarReject), name='raport_car_reject'),
# ex: lease/raports/end/32
    path('raports/end/<int:raport_id>', login_required(views.CarDone), name='raport_car_done'),
# ex: lease/raports/delete/32
    path('raports/delete/<int:raport_id>', login_required(views.ReportDelete), name='raport_delete'),

]