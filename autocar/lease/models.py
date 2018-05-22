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

class Raport(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    data = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    status = models.CharField('Status',max_length=20,default='W trakcie rozpatrywania')
    worker_accept = models.CharField('Pracownik przyjmujący',max_length=20,default='')
    worker = models.CharField('Pracownik wydający', max_length=20, default='')
    worker_reject = models.CharField('Pracownik odbierający',max_length=20,default='')
    active = models.BooleanField('Aktywny',default=True)
    class Meta:
        verbose_name = "Raport"
        verbose_name_plural = "Raporty"



    def __str__(self):
        return "%s  |  %s : %s" % (self.client, self.data, self.time)
