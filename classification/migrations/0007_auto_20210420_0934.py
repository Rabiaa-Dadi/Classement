# Generated by Django 3.1.6 on 2021-04-20 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0006_auto_20210419_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(choices=[('patient', 'PATIENT'), ('medecin', 'MEDECIN')], default=True, max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='roles',
        ),
        migrations.AddField(
            model_name='medecin',
            name='Compte',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='classification.compte'),
        ),
        migrations.AddField(
            model_name='patient',
            name='Compte',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='classification.compte'),
        ),
    ]
