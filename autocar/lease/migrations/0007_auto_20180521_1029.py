# Generated by Django 2.0.5 on 2018-05-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0006_raport_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='raport',
            name='status',
            field=models.CharField(default='', max_length=20, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='raport',
            name='worker',
            field=models.CharField(default='', max_length=20, verbose_name='Pracownik'),
        ),
    ]