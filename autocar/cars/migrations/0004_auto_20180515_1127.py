# Generated by Django 2.0.5 on 2018-05-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20180515_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.IntegerField(choices=[(1, 'Diesel'), (2, 'Benzyna'), (3, 'Benzyna + LPG')], max_length=20, verbose_name='Paliwo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='gearbox',
            field=models.IntegerField(choices=[(1, 'Manualna'), (2, 'Automatyczna'), (3, 'Pół Automatyczna')], max_length=20, verbose_name='Skrzynia biegów'),
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.IntegerField(choices=[(1, 'Hatchback'), (2, 'Sedan'), (3, 'Kombi'), (4, 'Sportowe | Coupe'), (5, 'Kabriolet'), (6, 'Limuzyna'), (7, 'Pickup'), (8, 'Terenowe'), (9, 'Van | Minibus')], max_length=20, verbose_name='Typ'),
        ),
    ]