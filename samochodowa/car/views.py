from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms import modelformset_factory
from .models import *


# Widok Strony głównej
# Home
def index(request):
    car = Car.objects.all()
    return render(request,'index.html',{'car_list': car})

# Widok Szczegółów wybranego Auta
#Detalis car
def details(request,car_id):
    car = Car.objects.get(pk=car_id)

    return render(request, 'details.html',{'car': car})


#Views add car
def add_car(request):

    if request.method == "POST":
        form = AddCar(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Dodano Samochód")
    else:
        form = AddCar()
    return render(request, 'add.html', {'form': form})

def add_ca(request):

    if request.method == "POST":
        form = AddCar(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Dodano Samochód")
    else:
        form = AddCar()
    return render(request, 'szablon_form.html', {'form': form})
