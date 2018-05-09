from django.db import models
from django.utils import timezone

# Create your models here.

class Auto(models.Model):
    model = models.CharField(max_length=20)
    marka = models.CharField(max_length=20)
    skrzynia = models.CharField(max_length=20)
    paliwo = models.CharField(max_length=20)
    typ = models.CharField(max_length=20)
    koszt = models.IntegerField()
    img = models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Car_with_Driver-Silhouette.svg/916px-Car_with_Driver-Silhouette.svg.png')

    def __str__(self):
        return self.model








