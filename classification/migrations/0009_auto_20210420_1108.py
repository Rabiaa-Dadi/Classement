# Generated by Django 3.1.6 on 2021-04-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0008_auto_20210420_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='sexe',
            field=models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], default=True, max_length=10),
        ),
    ]