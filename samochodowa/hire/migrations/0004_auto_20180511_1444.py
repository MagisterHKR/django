# Generated by Django 2.0.5 on 2018-05-11 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0003_remove_hire_kk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hire',
            old_name='Comments',
            new_name='comments',
        ),
    ]
