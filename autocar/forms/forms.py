
from django import forms
from cars.models import Car
from users.models import Client
from captcha.fields import ReCaptchaField

from django.contrib.auth.models import User


#Dodawanie auta
class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

class AddCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('model', 'mark', 'gearbox', 'fuel', 'type', 'description', 'charge', 'photo')




class user_register(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields=('username','password','first_name','last_name','email')



