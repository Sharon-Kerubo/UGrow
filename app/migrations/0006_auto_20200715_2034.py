# Generated by Django 3.0.8 on 2020-07-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_crop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='county_nam',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='crops',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='main_crop',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='other_crop',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='watering',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
