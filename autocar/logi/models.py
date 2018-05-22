from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Logi(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    action = models.CharField('Akcja:',max_length=30)
    raport = models.IntegerField('ID raportu')
    car = models.IntegerField('ID auta')
    addition = models.CharField('Dodatkowe',max_length=30,default='')

    class Meta:
        verbose_name = "Logi"
        verbose_name_plural = "Logi"


    def __str__(self):
        return "%s | %s " %(self.user,self.date)