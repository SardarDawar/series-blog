# Generated by Django 3.0.6 on 2021-02-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_auto_20210217_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comingsoon',
            name='PG',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='PG',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='newarrival',
            name='PG',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='PG',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='series',
            name='PG',
            field=models.CharField(max_length=20),
        ),
    ]