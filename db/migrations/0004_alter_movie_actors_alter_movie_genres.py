# Generated by Django 4.0.2 on 2023-10-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0003_rename_row_cinemahall_rows"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(related_name="actors", to="db.Actor"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(related_name="genres", to="db.Genre"),
        ),
    ]
