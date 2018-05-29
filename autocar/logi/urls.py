from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from lease.models import Raport
from . import views


urlpatterns = [

    path('', login_required(views.LogsListView.as_view()), name='logi'),


]