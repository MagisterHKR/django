from django.db import models

# Create your models here.

# Model Samochodu
class Car(models.Model):
    type_choice = (
        ('Hatchback', 'Hatchback'),
        ('Sedan', 'Sedan'),
        ('Kombi', 'Kombi'),
        ('Sportowe | Coupe', 'Sportowe | Coupe'),
        ('Kabriolet', 'Kabriolet'),
        ('Limuzyna', 'Limuzyna'),
        ('Pickup', 'Pickup'),
        ('Terenowe', 'Terenowe'),
        ('Van | Minibus', 'Van | Minibus'),
    )
    fuel_choice = (
        ('Diesel', 'Diesel'),
        ('Benzyna', 'Benzyna'),
        ('Benzyna + LPG', 'Benzyna + LPG'),
    )
    gearbox_choice = (
        ('Manualna', 'Manualna'),
        ('Automatyczna', 'Automatyczna'),
        ('Pół Automatyczna', 'Pół Automatyczna'),
    )
    model = models.CharField('Model', max_length=20)
    mark = models.CharField('Marka', max_length=20)
    gearbox = models.CharField('Skrzynia biegów', max_length=20, choices=gearbox_choice)
    fuel = models.CharField('Paliwo', max_length=20, choices=fuel_choice)
    type = models.CharField('Typ', max_length=20, choices=type_choice)
    description = models.CharField('Opis',max_length=60,default='Brak')
    charge = models.CharField('Koszt', max_length=20)
    photo = models.URLField('Zdjęcie', default='http://demo.sc.chinaz.com/Files/pic/icons/1499/chinaz3.png')
    checked = models.BooleanField('Wypożyczony', default=False)

    class Meta:
        verbose_name = "Samochód"
        verbose_name_plural = "Samochody"

    def __str__(self):
        return self.model
