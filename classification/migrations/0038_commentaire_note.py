# Generated by Django 3.1.6 on 2021-05-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0037_delete_dictionnaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='note',
            field=models.FloatField(default=0, null=True),
        ),
    ]