# Generated by Django 3.0.6 on 2021-02-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210210_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
