# Generated by Django 4.1.3 on 2022-11-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0002_car_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='car',
            field=models.ManyToManyField(to='autoservice.car_model'),
        ),
    ]
