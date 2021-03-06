# Generated by Django 3.0.6 on 2021-02-16 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_auto_20210216_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('bg_img', models.ImageField(upload_to='prod_imgs/')),
                ('PG', models.IntegerField()),
                ('quality', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
                ('length', models.CharField(max_length=10)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Genre')),
            ],
        ),
    ]
