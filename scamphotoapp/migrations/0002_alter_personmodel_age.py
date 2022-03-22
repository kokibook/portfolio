# Generated by Django 3.2.4 on 2022-03-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scamphotoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='age',
            field=models.CharField(choices=[('', '選択してください'), ('十代後半', '10代後半'), ('二十代前半', '20代前半'), ('二十代後半', '20後半'), ('三十代前半', '30代前半'), ('三十代後半', '30代後半'), ('四十代前半', '40代前半'), ('四十代後半', '40代後半'), ('五十代前半', '50代前半'), ('五十代後半', '50代後半'), ('六十代以上', '60代以上')], max_length=50, verbose_name='年齢'),
        ),
    ]