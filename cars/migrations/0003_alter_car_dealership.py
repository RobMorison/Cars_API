# Generated by Django 4.1.5 on 2023-01-17 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0001_initial'),
        ('cars', '0002_car_dealership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='dealership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dealerships.dealership'),
            preserve_default=False,
        ),
    ]
