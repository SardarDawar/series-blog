# Generated by Django 3.0.6 on 2021-02-11 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210212_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviecategory',
            name='icon_class',
        ),
        migrations.RemoveField(
            model_name='seriescategory',
            name='icon_class',
        ),
    ]