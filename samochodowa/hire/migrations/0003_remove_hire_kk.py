# Generated by Django 2.0.5 on 2018-05-11 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0002_hire_kk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hire',
            name='kk',
        ),
    ]