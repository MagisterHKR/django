from django.db import models
from django import forms


# Dodanie auta, za pomocą menadżera
class CarManager(models.Manager):
    def create(self,model,mark,gearbox,fuel,type,description,charge,photo,checked):
        car = self.create(model=model,mark=mark,gearbox=gearbox,fuel=fuel,type=type,description=description,charge=charge,photo=photo)
        return car




# Model Samochodu
class Car(models.Model):
    type_choice = (
        ('hh', 'Hatchback'),
        ('se', 'Sedan'),
        ('ko', 'Kombi'),
        ('sc', 'Sportowe | Coupe'),
        ('kb', 'Kabriolet'),
        ('li', 'Limuzyna'),
        ('pi', 'Pickup'),
        ('te', 'Terenowe'),
        ('vm', 'Van | Minibus'),
    )
    fuel_choice = (
        ('ON', 'Diesel'),
        ('PB', 'Benzyna'),
        ('PBLPG', 'Benzyna + LPG'),
    )
    gearbox_choice = (
        ('mm', 'Manualna'),
        ('aa', 'Automatyczna'),
        ('ma', 'Pół Automatyczna'),
    )
    model = models.CharField('Model', max_length=20)
    mark = models.CharField('Marka', max_length=20)
    gearbox = models.CharField('Skrzynia biegów', max_length=20, choices=gearbox_choice)
    fuel = models.CharField('Paliwo', max_length=20, choices=fuel_choice)
    type = models.CharField('Typ', max_length=20, choices=type_choice)
    description = models.CharField('Opis',max_length=60,default='Brak')
    charge = models.CharField('Koszt', max_length=20)
    photo = models.URLField('Zdjęcie', default='http://demo.sc.chinaz.com/Files/pic/icons/1499/chinaz3.png')
    checked = models.BooleanField('Wypożyczony', default=False)

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
            fields = ('model', 'mark', 'gearbox', 'fuel', 'type', 'description', 'charge', 'photo')

