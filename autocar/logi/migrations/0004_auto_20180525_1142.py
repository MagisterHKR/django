# Generated by Django 2.0.5 on 2018-05-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logi', '0003_auto_20180522_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logi',
            name='car',
            field=models.IntegerField(default='', verbose_name='ID auta'),
        ),
    ]
