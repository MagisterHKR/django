# Generated by Django 2.0.5 on 2018-05-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0008_auto_20180521_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='raport',
            name='worker_accept',
            field=models.CharField(default='', max_length=20, verbose_name='Pracownik'),
        ),
        migrations.AlterField(
            model_name='raport',
            name='status',
            field=models.CharField(default='W trakcie rozpatrzania', max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='raport',
            name='worker',
            field=models.CharField(default='', max_length=20, verbose_name='Pracownik'),
        ),
    ]