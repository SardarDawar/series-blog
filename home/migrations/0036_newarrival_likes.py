# Generated by Django 3.0.6 on 2021-02-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_comment_newarrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='newarrival',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
