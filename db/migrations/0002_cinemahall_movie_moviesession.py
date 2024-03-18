# Generated by Django 5.0.3 on 2024-03-18 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CinemaHall",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("rows", models.IntegerField()),
                ("seats_in_row", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("actors", models.ManyToManyField(to="db.actor")),
                ("genres", models.ManyToManyField(to="db.genre")),
            ],
        ),
        migrations.CreateModel(
            name="MovieSession",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("show_time", models.DateTimeField()),
                (
                    "cinema_hall",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="db.cinemahall",
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="db.movie",
                    ),
                ),
            ],
        ),
    ]
