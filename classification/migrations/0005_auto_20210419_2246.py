# Generated by Django 3.1.6 on 2021-04-19 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classification', '0004_auto_20210419_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medecin',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='nom',
        ),
        migrations.AlterField(
            model_name='compte',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]