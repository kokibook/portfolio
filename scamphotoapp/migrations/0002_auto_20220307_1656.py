# Generated by Django 3.2.4 on 2022-03-07 07:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scamphotoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='People',
            new_name='Peoplemodel',
        ),
        migrations.RenameModel(
            old_name='Photo',
            new_name='PhotoModel',
        ),
    ]
