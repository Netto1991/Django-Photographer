# Generated by Django 3.0.6 on 2020-06-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotopage', '0008_specialoffers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='aboutme',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='priceofwork',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='specialoffers',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
