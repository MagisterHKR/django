# Generated by Django 2.0.5 on 2018-05-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.URLField(default='http://demo.sc.chinaz.com/Files/pic/icons/1499/chinaz3.png', verbose_name='Zdjęcie'),
        ),
    ]