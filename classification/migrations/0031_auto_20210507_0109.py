# Generated by Django 3.1.6 on 2021-05-07 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0030_auto_20210506_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentaire',
            old_name='Medecin',
            new_name='medecin',
        ),
        migrations.RenameField(
            model_name='commentaire',
            old_name='Patient',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='medecin',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='medecin',
            old_name='Spécialité',
            new_name='spécialité',
        ),
        migrations.RenameField(
            model_name='medecin',
            old_name='Ville',
            new_name='ville',
        ),
    ]
