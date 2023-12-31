# Generated by Django 3.1.6 on 2021-04-19 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compte',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='medecin',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='Compte',
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='Spécialité',
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='Ville',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Compte',
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
        migrations.DeleteModel(
            name='Compte',
        ),
        migrations.DeleteModel(
            name='Medecin',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Spécialité',
        ),
        migrations.DeleteModel(
            name='Ville',
        ),
    ]
