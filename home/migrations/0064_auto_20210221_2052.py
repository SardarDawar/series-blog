# Generated by Django 3.1.6 on 2021-02-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_auto_20210221_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='comingsoon',
            name='rating',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newarrival',
            name='rating',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='rating',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='rating',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
