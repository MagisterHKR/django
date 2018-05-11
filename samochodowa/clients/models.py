from django.db import models

# Create your models here.

# dodawanie klienta
class ClientManager(models.Manager):
    def create(self,pesel,name,sur_name,tel):
        lender = self.create(pesel=pesel,name=name,sur_name=sur_name,tel=tel)
        return lender


# Model Klienta
class Client(models.Model):

    name = models.CharField('Imię',max_length=20)
    sur_name = models.CharField('Nazwisko',max_length=50)
    tel = models.CharField('Telefon',max_length=9)
    pesel = models.CharField('Pesel', max_length=11)

    objects = ClientManager()

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"

    def __str__(self):
        return self.name

