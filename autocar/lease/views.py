from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms import modelformset_factory
from django.views.generic import ListView,CreateView

from cars.models import Car
from users.models import Client
from .models import Lease,Raport
from logi.models import Logi


# Create your views here.



class RaportsListView(ListView):
    template_name = 'lease/raport_list.html'

    def get_queryset(self):
        return Raport.objects.all().order_by('-time')


class RaportCreateView(CreateView):
    model = Raport
    fields = '__all__'


def CreateRaport(request,car_id):

    user = request.user.client
    car = Car.objects.get(id=car_id)
    raport = Raport(client=user,car=car,status='W trakcie realizacji')
    raport.save()

    logi = Logi(user=request.user, action="Wypożyczenie auta",raport=raport.id,car=raport.car.id)
    logi.save()
    return render(request,'lease/success.html',{'data':raport.data})

def success(request):

    return render_to_response('lease/success.html')

def RaportDetail(request,raport_id):

    raport = Raport.objects.get(id=raport_id)
    user = Client.objects.get(nickname=raport.client)
    car = Car.objects.get(id=raport.car.id)

    return render(request,'lease/raport_detail.html',{'raport':raport,'car':car,'user':user})

def RaportAccept(request,raport_id):
    raport = Raport.objects.get(id=raport_id)
    raport.status='Gotowy do odbioru'
    raport.worker_accept=request.user.username
    raport.save()


    logi = Logi(user=request.user, action="Zatwierdzenie wypożyczenia auta",raport=raport.id,car=raport.car.id)
    logi.save()

    return render(request, 'lease/accept.html', {"status": raport.status})

def CarAcctept(request,raport_id):
    raport = Raport.objects.get(id=raport_id)
    raport.status = 'Wydany'
    raport.worker=request.user.username
    raport.save()
    car = Car.objects.get(id=raport.car.id)
    car.checked=True
    car.save()
    logi = Logi(user=request.user, action="Wypożyczenie auta",raport=raport.id,car=raport.car.id)
    logi.save()

    return render(request, 'lease/accept.html',{"status": raport.status})

def CarReject(request,raport_id):
    raport = Raport.objects.get(id=raport_id)
    raport.status = 'Odrzucony'
    raport.active = False
    raport.worker_accept=request.user.username
    raport.save()

    logi = Logi(user=request.user, action="Odrzucenie wniosku",raport=raport.id,car=raport.car.id)
    logi.save()
    return render(request, 'lease/accept.html',{"status": raport.status})

def CarDone(request,raport_id):

    raport = Raport.objects.get(id=raport_id)
    raport.status = 'Odebrany'
    raport.worker_reject=request.user.username
    raport.active = False
    raport.save()
    car = Car.objects.get(id=raport.car.id)
    car.checked = False
    car.save()

    logi = Logi(user=request.user, action="Odebranie auta od klienta",raport=raport.id,car=car.id)
    logi.save()

    return render(request, 'lease/accept.html',{"status": raport.status})