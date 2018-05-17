from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms import modelformset_factory
from django.views import generic

from .models import Lease


# Create your views here.


def lease_details(request):
    pass
