# Generated by Django 3.2.9 on 2021-11-08 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0011_alter_favorites_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
