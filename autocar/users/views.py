import json
import urllib


from django.shortcuts import render, redirect
from django.conf import settings

from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User



from forms.forms import user_register
from users.models import Client


def profil(request):

    return render(request, 'users/profil.html')

def list_profil(request):
    client = User.objects.all()
    return render(request, 'users/list_profile.html',{'user_list': client})


def reg_succ(request):
    return render(request, 'users/register_success.html')

def registration(request):
    form = user_register()
    if request.method == 'POST':
        form = user_register(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if "admin" in username.lower():
                info = 'Użytkownik nie może mieć prefiksu admin'
                return render(request, 'users/register.html', {"info": info})
            user = auth.authenticate(username=username, password=password)
            if user is None:
                form.save()
                return HttpResponseRedirect('succes')
            else:
                info = 'Użytkownik już istnieje'
                return render(request, 'users/register.html', {"info": info})
        else:
            info = 'Uzupełnij wszystkie pola'
            return render(request, 'users/register.html', {'form': form,"info": info})
    else:
        return render(request, 'users/register.html', {'form': form})



def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/profil/logged/')
        else:
            info = 'Błędne dane logowania'
            return render(request, 'users/login.html',{"info":info})
    else:
        return render(request, 'users/login.html')








def logout(request):
    auth.logout(request)
    return render_to_response('users/logout.html')

def logged(request):

    return render(request, 'users/logged.html')

