# Generated by Django 3.0.6 on 2021-02-09 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210210_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('img1', models.ImageField(upload_to='prod_imgs/')),
                ('img2', models.ImageField(upload_to='prod_imgs/')),
                ('img3', models.ImageField(upload_to='prod_imgs/')),
                ('img4', models.ImageField(upload_to='prod_imgs/')),
                ('rating', models.FloatField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Content')),
            ],
        ),
    ]
