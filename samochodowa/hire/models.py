from django.db import models
from django import forms

from car.models import Car
from clients.models import Client
# Create your models here.

# wypożyczenia
class Hire(models.Model):
    lender = models.ForeignKey(Client,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    title = models.CharField('Tytuł',max_length=30)
    comments = models.TextField('Uwagi')
    data = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Wypożyczenie"
        verbose_name_plural = "Wypożyczenia"

    def __str__(self):
        return self.title



class AddHire(forms.ModelForm):
    class Meta:
        model = Hire
        fields = ('lender','car','title','comments')
