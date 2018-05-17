from django.db import models

# Create your models here.
from cars.models import Car
from users.models import Client


class Lease(models.Model):
    lender = models.ForeignKey(Client,on_delete=models.CASCADE)
    car = models.OneToOneField(Car,on_delete=models.CASCADE)
    title = models.CharField('Tytuł',max_length=30)
    comments = models.TextField('Uwagi')
    data = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Wypożyczenie"
        verbose_name_plural = "Wypożyczenia"

    def __str__(self):
        return self.title
