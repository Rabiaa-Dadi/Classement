# Generated by Django 3.1.6 on 2021-04-25 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0022_auto_20210426_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Medecin',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Patient',
        ),
        migrations.AddField(
            model_name='contact',
            name='Compte',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='classification.compte'),
        ),
    ]
