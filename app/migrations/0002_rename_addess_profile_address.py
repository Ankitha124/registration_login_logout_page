# Generated by Django 4.2.2 on 2023-07-19 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='addess',
            new_name='address',
        ),
    ]
