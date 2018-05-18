from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms import modelformset_factory
from django.views.generic import ListView,CreateView

from cars.models import Car
from users.models import Client
from .models import Lease,Raport


# Create your views here.


def lease_details(request):
    pass

class RaportsListView(ListView):
    template_name = 'lease/raport_list.html'

    def get_queryset(self):
        return Raport.objects.all()


class RaportCreateView(CreateView):
    model = Raport
    fields = '__all__'


def CreateRaport(request,car_id):
    user = request.user.client

    car = Car.objects.get(id=car_id)
    report = Raport(client=user,car=car)
    report.save()
    return render(request,'lease/success.html',{'data':report.data})

def success(request):

    return render_to_response('lease/success.html')