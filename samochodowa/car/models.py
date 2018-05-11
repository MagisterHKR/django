from django.db import models
from django import forms


# Model Samochodu
class CarManager(models.Manager):
    def create(self,model,mark,gearbox,fuel,type,charge,photo,checked):
        car = self.create(model=model,mark=mark,gearbox=gearbox,fuel=fuel,type=type,charge=charge,photo=photo)
        return car




class Car(models.Model):
    model = models.CharField('Model',max_length=20)
    mark = models.CharField('Marka',max_length=20)
    gearbox = models.CharField('Skrzynia biegów',max_length=20)
    fuel = models.CharField('Paliwo',max_length=20)
    type = models.CharField('Typ',max_length=20)
    charge = models.CharField('Koszt',max_length=20)
    photo = models.URLField('Zdjęcie',default='http://demo.sc.chinaz.com/Files/pic/icons/1499/chinaz3.png')
    checked = models.BooleanField('Wypożyczony',default=False)

    objects=CarManager()



    class Meta:
        verbose_name = "Samochód"
        verbose_name_plural = "Samochody"

    def __str__(self):
        return self.model



#Dodawanie auta
class AddCar(forms.ModelForm):
        class Meta:
            model = Car
            fields = ('model', 'mark', 'gearbox', 'fuel', 'type', 'charge', 'photo')
