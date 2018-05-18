# Generated by Django 2.0.5 on 2018-05-18 07:15

import cars.models
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0002_auto_20180515_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=50, verbose_name=users.models.Client)),
                ('car', models.CharField(max_length=30, verbose_name=cars.models.Car)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Raport',
                'verbose_name_plural': 'Raporty',
            },
        ),
    ]