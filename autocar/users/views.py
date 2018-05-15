from django.shortcuts import render
from forms.forms import UserForm, ProfileForm
from .models import User

# Create your views here.

def profil(request):
	car = User.objects.all()
    return render(request,'cars/index.html',{'car_list': car})