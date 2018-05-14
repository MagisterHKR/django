from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import *
# Create your views here.


# Widok Strony głównej Oferty
def index(request):
    car = Car.objects.all()
    return render(request,'index.html',{'car_list': car})


# Widok Szczegółów wybranego Auta
def details(request,car_id):
    car = Car.objects.get(pk=car_id)

    return render(request, 'details.html',{'car': car})

def add_car(request):
    if request.method == "POST":
        form = AddCar(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Dodano Samochód")
    else:
        form = AddCar()
    return render(request, 'add.html', {'form': form})