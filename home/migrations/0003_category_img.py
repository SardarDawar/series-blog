# Generated by Django 3.0.6 on 2021-02-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(default=0, upload_to='prod_imgs/'),
            preserve_default=False,
        ),
    ]
