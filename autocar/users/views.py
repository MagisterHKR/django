import json
import urllib


from django.shortcuts import render, redirect
from django.conf import settings

from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User



from forms.forms import user_register, FormWithCaptcha
from users.models import Client


def profil(request):
    if Client.objects.filter(nickname=request.user.username).first():
        return render(request, 'users/profil.html')
    else:
        Client(user=request.user, nickname=request.user.username).save()
        return render(request, 'users/profil.html')

def list_profil(request):
    client = User.objects.all()
    return render(request, 'users/list_profile.html',{'user_list': client})


def reg_succ(request):
    return render(request, 'users/register_success.html')

def registration(request):
    form = user_register()

    if request.method == 'POST':

        form = FormWithCaptcha(request.POST)
        if form.is_valid():

            username = request.POST['username']
            password = request.POST['pass1']
            password2 = request.POST['pass2']
            email = request.POST['email']
            f_name =request.POST['first_name']
            l_name = request.POST['last_name']

            if "admin" in username.lower():
                info = 'Użytkownik nie może mieć prefiksu admin'

                return render(request, 'users/register.html', {'form': form,"info": info})

            user = auth.authenticate(username=username, password=password)
            if user is None:
                if password == password2:
                    user = User.objects.create_user(username,email,password)
                    user.last_name = l_name
                    user.first_name = f_name
                    client = Client(user=user,nickname=username)
                    client.save()
                    user.save()
                    return HttpResponseRedirect('succes')
                else:
                    info = 'Hasła się różnią'
                    return render(request, 'users/register.html',{'form': form,"info": info})


            else:
                info = 'Użytkownik już istnieje'
                return render(request, 'users/register.html', {'form': form,"info": info})
        else:
            info = 'Uzupełnij wszystkie pola'
            return render(request, 'users/register.html', {'form': form,"info": info})
    else:
        return render(request, 'users/register.html', {'form': form,})



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


def profil_id(request,user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/profil.html',{'user':user})

def edit_profile(request,user_id):

    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = User.objects.all().get(id=user_id)
        user.client.nickname = request.POST['nickname']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        client = user.client
        client.tel = request.POST['tel']
        client.pesel = request.POST['pesel']
        client.avatar = request.POST['avatar']
        client.save()
        return render(request,'users/profil.html')

    else:
        user = User.objects.all().get(id=user_id)

        return render(request,'users/edit_user.html',{'user':user})
