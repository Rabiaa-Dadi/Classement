# Generated by Django 4.2.7 on 2023-11-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0039_auto_20210527_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='rate',
            field=models.PositiveSmallIntegerField(default=True, max_length=5),
        ),
    ]
