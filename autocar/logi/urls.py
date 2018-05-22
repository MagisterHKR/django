from django.urls import path

from lease.models import Raport
from . import views


urlpatterns = [

    path('', views.LogsListView.as_view(), name='logi'),


]