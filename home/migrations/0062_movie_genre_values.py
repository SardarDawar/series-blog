# Generated by Django 3.1.6 on 2021-02-18 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_auto_20210219_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre_values',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
