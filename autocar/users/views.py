from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.

def profil(request):

    return render(request, 'users/profil.html')

def list_profil(request):
    client = User.objects.all()
    return render(request, 'users/list_profile.html',{'user_list': client})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/profil/logged/')
    else:
        return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('users/logout.html')

def logged(request):

    return render(request, 'users/logged.html')