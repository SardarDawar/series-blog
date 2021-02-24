# Generated by Django 3.1.6 on 2021-02-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0066_remove_movie_genre_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='quality',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='size',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]