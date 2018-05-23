from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView

from django.shortcuts import render

# Create your views here.
from .models import Logi


class LogsListView(ListView):
    template_name = 'logi/logi.html'
    model = Logi
    context_object_name = "logi_list"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(LogsListView, self).get_context_data(**kwargs)
        car_list = Logi.objects.all().order_by('-date')
        paginator = Paginator(car_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['logi_list'] = file_exams
        return context