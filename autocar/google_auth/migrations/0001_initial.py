# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 22:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('token_expiry', models.DateTimeField()),
                ('access_token', models.CharField(max_length=254)),
                ('refresh_token', models.CharField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='google_auth_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
