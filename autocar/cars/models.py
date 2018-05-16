from django.db import models

# Create your models here.

# Model Samochodu
class Car(models.Model):

    type_choice = (
        (1, 'Hatchback'),
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
    mark = models.CharField('Marka', max_length=20)
    gearbox = models.IntegerField('Skrzynia biegów', choices=gearbox_choice)
    fuel = models.IntegerField('Paliwo', choices=fuel_choice)
    type = models.IntegerField('Typ', choices=type_choice)
    description = models.CharField('Opis',max_length=60,default='Brak')
    charge = models.CharField('Koszt', max_length=20)
    photo = models.URLField('Zdjęcie', default='https://www.freeiconspng.com/uploads/sport-car-icon-0.png')
    checked = models.BooleanField('Wypożyczony', default=False)

    class Meta:
        verbose_name = "Samochód"
        verbose_name_plural = "Samochody"

    def __str__(self):
        return self.model
