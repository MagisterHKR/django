from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import *
# Create your views here.
#Views add car
def add_hire(request):

    if request.method == "POST":
        form = AddHire(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Dodano")
    else:
        form = AddHire()
    return render(request, 'add.html', {'form': form})


def test(request):
    if request.method == "POST":
        pass
