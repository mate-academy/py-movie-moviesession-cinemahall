# Generated by Django 4.0.2 on 2023-10-14 15:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0002_cinemahall_movie_moviesession"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cinemahall",
            old_name="seats_in_rows",
            new_name="seats_in_row",
        ),
    ]
