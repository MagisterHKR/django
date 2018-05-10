from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.

# dodawanie klienta
class LenderManager(models.Manager):
    def create(self,pesel,name,sur_name,tel):
        lender = self.create(pesel=pesel,name=name,sur_name=sur_name,tel=tel)
        return lender

# Samochód
class Auto (models.Model):
    model = models.CharField('Model',max_length=20)
    mark = models.CharField('Marka',max_length=20)
    gearbox = models.CharField('Skrzynia biegów',max_length=20)
    fuel = models.CharField('Paliwo',max_length=20)
    type = models.CharField('Typ',max_length=20)
    charge = models.CharField('Koszt',max_length=20)
    photo = models.URLField('Zdjęcie',default='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Car_with_Driver-Silhouette.svg/916px-Car_with_Driver-Silhouette.svg.png')
    checked = models.BooleanField('Wypożyczony',default=False)


    class Meta:
        verbose_name = "Samochód"
        verbose_name_plural = "Samochody"

    def __str__(self):
        return self.model

# wypożyczający
class Lender(models.Model):

    name = models.CharField('Imię',max_length=20)
    sur_name = models.CharField('Nazwisko',max_length=50)
    tel = models.CharField('Telefon',max_length=9)
    pesel = models.CharField('Pesel', max_length=11)

    objects = LenderManager()

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"

    def __str__(self):
        return self.name

# wypożyczenia
class Hire(models.Model):
    lender = models.ForeignKey(Lender,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    title = models.CharField('Tytuł',max_length=30)
    Comments = models.CharField('Uwagi',max_length=30)
    data = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Wypożyczenie"
        verbose_name_plural = "Wypożyczenia"

    def __str__(self):
        return self.title



# formularz dodawania samochodu
class AddCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('model','mark','gearbox','fuel','type','charge','photo')