from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User



from forms.forms import user_register, FormWithCaptcha
from users.models import Client

#User profile view
def profil(request):
    return render(request, 'users/profil.html')
#View all users
def list_profil(request):
    client = User.objects.all()
    return render(request, 'users/list_profile.html',{'user_list': client})

#View after correct registration
def reg_succ(request):
    return render(request, 'users/register_success.html')
#Registration support
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
                    return HttpResponseRedirect('profil')
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


#Login support
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/profil/')
        else:
            info = 'Błędne dane logowania'
            return render(request, 'users/login.html',{"info":info})
    else:
        return render(request, 'users/login.html')


#User logout
def logout(request):
    auth.logout(request)
    return render_to_response('users/logout.html')


#User profile view with 'id' specified
def profil_id(request,user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/profil.html',{'user':user})
# Editing a user with 'id' specified
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
        return render(request,'users/profil.html',{'user':user})

    else:
        user = User.objects.get(id=user_id)

        return render(request,'users/edit_user.html',{'user':user})
#Password change
def password_chnge(request):
    if request.method == 'POST':
        activ_pass = request.POST['activ_pass']
        if request.user.check_password(activ_pass):
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1 == pass2:
                user = User.objects.get(username=request.user.username)
                user.set_password(pass1)
                user.save()
                info = 'Hasło zmieione.'
                return render(request, 'users/profil.html', {'info': info})
            else:
                info = "Hasła nie są zgodne."
                return render(request, 'users/edit_password.html', {'info': info})
        else:
            info = "Hasło nie prawidłowe"
            return render(request, 'users/edit_password.html', {'info': info})
    else:
        return render(request, 'users/edit_password.html')

#Creating a password after logging in by Google
def create_password(request):
    if request.user.password is not None:
        info = 'Zalogowano za pomocą Google.'
        return render(request, 'users/profil.html', {'info': info})
    else:
        if request.method == 'POST':
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1 == pass2:
                request.user.set_password(pass1)
                info = 'Hasło utworzone.'
                client = Client(user=request.user, nickname=request.user.username)
                client.save()
                return render(request, 'users/profil.html', {'info': info})
            else:
                info = "Hasła nie są zgodne."
                return render(request, 'users/create_password.html', {'info': info})
        else:
            return render(request, 'users/create_password.html')