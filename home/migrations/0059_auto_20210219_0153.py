# Generated by Django 3.1.6 on 2021-02-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_auto_20210218_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img_url',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='poster_url',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]