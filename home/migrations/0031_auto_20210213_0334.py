# Generated by Django 3.0.6 on 2021-02-12 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20210213_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist_items',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Playlist'),
        ),
    ]