# Generated by Django 3.1.6 on 2021-02-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0059_auto_20210219_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(blank=True, upload_to='prod_imgs/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='img_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='likes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, upload_to='prod_imgs/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_url',
            field=models.URLField(blank=True),
        ),
    ]
