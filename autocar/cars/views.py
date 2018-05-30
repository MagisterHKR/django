
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


from .models import Car






#Car list view
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




#Detail view of a given car
class CarDetailView(DetailView):
    template_name = 'cars/car_detail.html'
    pk_url_kwarg = "car_id"
    def get_queryset(self):
        return Car.objects.filter()



#View of creating a new car
class CarCreateView(CreateView):
    model = Car
    fields = '__all__'


    def form_valid(self, form):
        model = form.save(commit=False)
        print(type(model))
        return super(CarCreateView, self).form_valid(form)

#Editing view of a given car
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

