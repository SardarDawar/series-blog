# Generated by Django 3.0.6 on 2021-02-16 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_slidercategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.SliderCategory'),
            preserve_default=False,
        ),
    ]
