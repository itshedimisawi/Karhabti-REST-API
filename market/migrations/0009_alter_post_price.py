# Generated by Django 3.2.9 on 2021-11-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_auto_20211106_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]