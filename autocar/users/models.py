from django.db import models
from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
#https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField('Nick',max_length=20,default='Nowy')
    tel = models.CharField('Telefon',max_length=9)
    pesel = models.CharField('Pesel', max_length=11)
    group = models.CharField('Grupa',max_length=20,default='Klient')
    avatar = models.URLField('Avatar',default='http://www.winhelponline.com/blog/wp-content/uploads/2017/12/user.png')
    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"

    def __str__(self):
        return self.nickname

    def is_created(user):
        if Client.objects.all().get(nickname=user):
            return True
        else:
            return False