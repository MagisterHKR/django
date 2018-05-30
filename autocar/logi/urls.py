from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
<<<<<<< HEAD

=======
from lease.models import Raport
>>>>>>> 7760546998b33c19420eee8164288752cfa3a93d
from . import views


urlpatterns = [
<<<<<<< HEAD
# ex: logi/
=======

>>>>>>> 7760546998b33c19420eee8164288752cfa3a93d
    path('', login_required(views.LogsListView.as_view()), name='logi'),


]