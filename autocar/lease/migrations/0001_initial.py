# Generated by Django 2.0.5 on 2018-05-15 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0005_auto_20180515_1151'),
        ('users', '0004_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Tytuł')),
                ('comments', models.TextField(verbose_name='Uwagi')),
                ('data', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
                ('lender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Client')),
            ],
            options={
                'verbose_name': 'Wypożyczenie',
                'verbose_name_plural': 'Wypożyczenia',
            },
        ),
    ]