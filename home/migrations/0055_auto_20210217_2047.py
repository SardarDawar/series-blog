# Generated by Django 3.1.6 on 2021-02-17 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_slider_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='url',
            new_name='watch',
        ),
    ]