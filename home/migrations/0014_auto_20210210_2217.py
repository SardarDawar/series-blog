# Generated by Django 3.0.6 on 2021-02-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210210_0457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['orderBy']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-dateAdded']},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['orderBy']},
        ),
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ['orderBy']},
        ),
        migrations.AddField(
            model_name='category',
            name='orderBy',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='orderBy',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episode',
            name='orderBy',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]