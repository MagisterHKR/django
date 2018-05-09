from django.db import models
from django.utils import timezone

# Create your models here.
# Samochód
class Auto(models.Model):
    model = models.CharField(max_length=20)
    marka = models.CharField(max_length=20)
    skrzynia = models.CharField(max_length=20)
    paliwo = models.CharField(max_length=20)
    typ = models.CharField(max_length=20)
    koszt = models.CharField(max_length=20)
    img = models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Car_with_Driver-Silhouette.svg/916px-Car_with_Driver-Silhouette.svg.png')

    def __str__(self):
        return self.model
# wypożyczający
class Lender(models.Model):
    pesel = models.CharField(max_length=11)
    name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=50)
    tel = models.CharField(max_length=9)

    def __str__(self):
        return self.pesel



