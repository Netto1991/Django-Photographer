# Generated by Django 3.0.6 on 2020-06-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotopage', '0009_auto_20200608_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='aboutme',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='specialoffers',
            name='description',
            field=models.TextField(),
        ),
    ]
