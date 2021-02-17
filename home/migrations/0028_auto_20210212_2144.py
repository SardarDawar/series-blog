# Generated by Django 3.0.6 on 2021-02-12 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20210212_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaylistCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={},
        ),
        migrations.AlterModelOptions(
            name='moviecategory',
            options={},
        ),
        migrations.AlterModelOptions(
            name='seriescategory',
            options={},
        ),
        migrations.RemoveField(
            model_name='genre',
            name='orderBy',
        ),
        migrations.RemoveField(
            model_name='moviecategory',
            name='orderBy',
        ),
        migrations.RemoveField(
            model_name='seriescategory',
            name='orderBy',
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('img', models.ImageField(upload_to='prod_imgs/')),
                ('rating', models.FloatField()),
                ('orderBy', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.PlaylistCategory')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Genre')),
            ],
            options={
                'ordering': ['-orderBy'],
            },
        ),
        migrations.CreateModel(
            name='ComingSoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('img', models.ImageField(upload_to='prod_imgs/')),
                ('rating', models.FloatField()),
                ('orderBy', models.FloatField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Genre')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.MovieCategory')),
                ('playlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.PlaylistCategory')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.SeriesCategory')),
            ],
            options={
                'ordering': ['-orderBy'],
            },
        ),
    ]