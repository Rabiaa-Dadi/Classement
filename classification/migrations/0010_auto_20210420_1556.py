# Generated by Django 3.1.6 on 2021-04-20 14:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classification', '0009_auto_20210420_1108'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Compte',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='medecin',
            old_name='Compte',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Compte',
            new_name='Profile',
        ),
    ]