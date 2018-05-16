
from django import forms
from cars.models import Car

from django.contrib.auth.models import User


#Dodawanie auta


class AddCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('model', 'mark', 'gearbox', 'fuel', 'type', 'description', 'charge', 'photo')




