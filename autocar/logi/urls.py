from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views


urlpatterns = [
# ex: logi/
    path('', login_required(views.LogsListView.as_view()), name='logi'),


]