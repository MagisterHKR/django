# Generated by Django 2.0.5 on 2018-05-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0002_remove_auto_wypozyczony'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='img',
            field=models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Car_with_Driver-Silhouette.svg/916px-Car_with_Driver-Silhouette.svg.png'),
        ),
    ]
