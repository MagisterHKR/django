
from django import forms
from cars.models import Car



#Dodawanie auta
class AddCar(forms.ModelForm):
        class Meta:
            model = Car
            fields = ('model', 'mark', 'gearbox', 'fuel', 'type', 'description', 'charge', 'photo')