from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import Client
from django.contrib.auth.models import User
# Create your views here.

def profil(request):

    return render(request, 'users/profile.html')

def list_profil(request):
    client = User.objects.all()
    return render(request, 'users/list_profile.html',{'user_list': client})

