# Generated by Django 3.2.9 on 2021-11-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0019_auto_20211113_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mileage',
            field=models.IntegerField(null=True),
        ),
    ]
