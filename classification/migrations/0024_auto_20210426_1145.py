# Generated by Django 3.1.6 on 2021-04-26 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classification', '0023_auto_20210426_0055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Compte',
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
