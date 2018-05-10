from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import *
# Create your views here.


# Widok Strony głównej Oferty
def index(request):
    car = Auto.objects.all()
    return render(request,'index.html',{'car_list': car})


# Widok Szczegółów wybranego Auta
def details(request,auto_id):
    auto_id = Auto.objects.get(pk=auto_id)

    return render(request, 'details.html',{'car': auto_id})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponse("Test")
    else:
        form = PostForm()
    return render(request, 'add.html', {'form': form})