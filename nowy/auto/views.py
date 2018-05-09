from django.shortcuts import render
from django.http import HttpResponse
from .models import Auto
# Create your views here.
# Widok Strony głównej Oferty
def index(request):
    car = Auto.objects.all()
    return render(request,'index.html',{'car_list': car})
# Widok Szczegółów wybranego Auta
def details(request,auto_id):
    auto_id = Auto.objects.get(pk=auto_id)

    return render(request, 'details.html',{'car': auto_id})