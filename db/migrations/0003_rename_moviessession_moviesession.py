# Generated by Django 4.0.2 on 2024-03-12 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_cinemahall_movie_moviessession'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MoviesSession',
            new_name='MovieSession',
        ),
    ]
