from django.views.generic import ListView

from django.shortcuts import render

# Create your views here.
from .models import Logi


class LogsListView(ListView):
    template_name = 'logi/logi.html'

    def get_queryset(self):
        return Logi.objects.all().order_by('-date')