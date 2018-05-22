from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponse

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from logi.models import Logi
from .models import Car
from forms.forms import AddCar
from django.urls import reverse

# Widok Strony głównej
# Home
#def car_index(request):
 #   car = Car.objects.all()
  #  return render(request,'cars/index.html',{'car_list': car})

# Widok Szczegółów wybranego Auta
#Detalis car


# Widok dodania nowego auta
#Views add car
def add_car(request):

    if request.method == "POST":
        form = AddCar(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponse("Dodano Samochód")
    else:
        form = AddCar()
    return render(request, 'cars/add.html', {'form': form})



#generyczne
class CarListView(ListView):
    template_name = 'cars/car_list.html'

    def get_queryset(self):
        return Car.objects.all()


class CarDetailView(DetailView):
    template_name = 'cars/car_detail.html'
    pk_url_kwarg = "car_id"
    def get_queryset(self):
        return Car.objects.filter()

def report(request,car_id):
    car = Car.objects.get(id=car_id)
    user = request.user



class CarCreateView(CreateView):
    model = Car
    fields = '__all__'

    def form_valid(self, form):
        model = form.save(commit=False)
        print(type(model))
        return super(CarCreateView, self).form_valid(form)


class CarUpdateView(UpdateView):
    model = Car
    fields = '__all__'
    pk_url_kwarg = "car_id"
    slug_url_kwarg = 'slug'
    template_name = 'cars/car_update_form.html'
    def form_valid(self, form):
        model = form.save(commit=False)

        print(type(model))
        return super(CarUpdateView, self).form_valid(form)

