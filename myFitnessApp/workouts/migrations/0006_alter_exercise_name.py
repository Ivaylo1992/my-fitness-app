# Generated by Django 5.1.6 on 2025-03-13 03:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workouts", "0005_exerciselog_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercise",
            name="name",
            field=models.CharField(
                max_length=50, validators=[django.core.validators.MinLengthValidator(5)]
            ),
        ),
    ]
