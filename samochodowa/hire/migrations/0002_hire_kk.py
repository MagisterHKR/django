# Generated by Django 2.0.5 on 2018-05-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='kk',
            field=models.BooleanField(default=False, verbose_name='test'),
        ),
    ]
