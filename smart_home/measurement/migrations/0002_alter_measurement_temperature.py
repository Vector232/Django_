# Generated by Django 4.2.6 on 2023-10-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="temperature",
            field=models.FloatField(),
        ),
    ]
