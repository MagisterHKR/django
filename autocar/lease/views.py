from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response
from django.views.generic import ListView,CreateView
from cars.models import Car
from users.models import Client
from .models import Raport
from logi.models import Logi


#View all reports
class RaportsListView(ListView):
    template_name = 'lease/raport_list.html'
    model = Raport
    context_object_name = "raport_list"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(RaportsListView, self).get_context_data(**kwargs)
        car_list = Raport.objects.all().order_by('-time')
        paginator = Paginator(car_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['raport_list'] = file_exams
        return context


#Creating a new report when renting a car
def CreateRaport(request,car_id):

    user = request.user.client
    car = Car.objects.get(id=car_id)
    car.reservation=True
    car.save()
    raport = Raport(client=user,car=car,status='W trakcie realizacji')
    raport.save()

    logi = Logi(user=request.user, action="Wypożyczenie auta",raport=raport.id,car=raport.car.id)
    logi.save()
    return render(request,'lease/success.html',{'data':raport.data})
#Information after placing the rental
def success(request):

    return render_to_response('lease/success.html')
#Details of the 'id' report
def RaportDetail(request,raport_id):

    raport = Raport.objects.get(id=raport_id)
    user = Client.objects.get(nickname=raport.client)
    car = Car.objects.get(id=raport.car.id)

    return render(request,'lease/raport_detail.html',{'raport':raport,'car':car,'user':user})
#Accepting a loan
def RaportAccept(request,raport_id):
    raport = Raport.objects.get(id=raport_id)
    raport.status='Gotowy do odbioru'
    raport.worker_accept=request.user.username
    raport.save()
    car = Car.objects.get(id=raport.car.id)
    car.reservation=False
    car.save()

    logi = Logi(user=request.user, action="Zatwierdzenie wypożyczenia auta",raport=raport.id,car=raport.car.id)
    logi.save()

    return render(request, 'lease/accept.html', {"status": raport.status})
#Car rental
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

#Rejection of the car rental application
def CarReject(request,raport_id):
    raport = Raport.objects.get(id=raport_id)
    raport.status = 'Odrzucony'
    raport.active = False
    raport.worker_accept=request.user.username
    raport.save()
    car = Car.objects.get(id=raport.car.id)
    car.reservation = False
    car.save()
    logi = Logi(user=request.user, action="Odrzucenie wniosku",raport=raport.id,car=raport.car.id)
    logi.save()
    return render(request, 'lease/accept.html',{"status": raport.status})

#Picking up the car from the customer
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
#Delete the report
def ReportDelete(request,raport_id):
    raport = Raport.objects.get(id=raport_id)
    raport.deleted = True
    raport.status = 'Usunięty'
    raport.save()
    logi = Logi(user=request.user, action="Usunięcie raportu",raport=raport.id,car=raport.car.id)
    logi.save()

    return render(request, 'lease/accept.html',{'status':raport.status})