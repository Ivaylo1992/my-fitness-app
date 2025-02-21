# Generated by Django 5.1.6 on 2025-02-21 03:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_food_calories_alter_food_carbohydrates_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='carbohydrates',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='food',
            name='fats',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='food',
            name='serving_size',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
