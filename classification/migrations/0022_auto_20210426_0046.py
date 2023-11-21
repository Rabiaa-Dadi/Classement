# Generated by Django 3.1.6 on 2021-04-25 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0021_remove_contact_compte'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Medecin',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='classification.medecin'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Patient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='classification.patient'),
        ),
    ]