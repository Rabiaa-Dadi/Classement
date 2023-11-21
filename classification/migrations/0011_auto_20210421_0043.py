# Generated by Django 3.1.6 on 2021-04-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0010_auto_20210420_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roles',
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('patient', 'PATIENT'), ('medecin', 'MEDECIN')], null=True),
        ),
    ]
