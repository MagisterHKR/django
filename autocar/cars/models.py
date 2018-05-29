from django.db import models

# Create your models here.
from django.urls import reverse



# Model Samochodu
class Car(models.Model):
    HB=1
    type_choice = (
        (HB, 'Hatchback'),
        (2, 'Sedan'),
        (3, 'Kombi'),
        (4, 'Sportowe | Coupe'),
        (5, 'Kabriolet'),
        (6, 'Limuzyna'),
        (7, 'Pickup'),
        (8, 'Terenowe'),
        (9, 'Van | Minibus'),
    )
    fuel_choice = (
        (1, 'Diesel'),
        (2, 'Benzyna'),
        (3, 'Benzyna + LPG'),
    )
    gearbox_choice = (
        (1, 'Manualna'),
        (2, 'Automatyczna'),
        (3, 'Pół Automatyczna'),
    )
    model = models.CharField('Model', max_length=20)
    number_plate = models.CharField('Rejestracja',max_length=20,default='BS -----')
    mark = models.CharField('Marka', max_length=20)
    gearbox = models.SmallIntegerField('Skrzynia biegów', choices=gearbox_choice)
    fuel = models.SmallIntegerField('Paliwo', choices=fuel_choice)
    type = models.SmallIntegerField('Typ', choices=type_choice)
    description = models.CharField('Opis',max_length=60,default='Brak')
    charge = models.CharField('Koszt', max_length=20)
    photo = models.URLField('Zdjęcie', default='https://www.freeiconspng.com/uploads/sport-car-icon-0.png')
    checked = models.BooleanField('Wypożyczony', default=False)
    reservation = models.BooleanField('Rezerwacja',default=False)

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'car_id': self.pk})

    class Meta:
        verbose_name = "Samochód"
        verbose_name_plural = "Samochody"

    def __str__(self):
        return self.model

