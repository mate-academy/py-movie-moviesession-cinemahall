# Generated by Django 4.0.2 on 2023-09-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_cinemahall_movie_moviesession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemahall',
            name='rows',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cinemahall',
            name='seats_in_row',
            field=models.IntegerField(default=0),
        ),
    ]
