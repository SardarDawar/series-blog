# Generated by Django 3.1.6 on 2021-02-22 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_auto_20210221_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='fname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='fsid',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='fsize',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='length',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='meta_name',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True, default="2021-02-02 16:53"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='time_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
