# Generated by Django 3.0.6 on 2021-02-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_newarrival_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecategory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='prod_imgs/'),
        ),
    ]