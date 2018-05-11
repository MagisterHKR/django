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
class Car (models.Model):
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







# formularz dodawania samochodu
