from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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




#generyczne
class CarListView(ListView):
    template_name = 'cars/car_list.html'
    model = Car
    context_object_name = "car_list"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        car_list = Car.objects.all()
        paginator = Paginator(car_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['car_list'] = file_exams
        return context





class CarDetailView(DetailView):
    template_name = 'cars/car_detail.html'
    pk_url_kwarg = "car_id"
    def get_queryset(self):
        return Car.objects.filter()




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

