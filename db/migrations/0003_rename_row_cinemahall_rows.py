# Generated by Django 4.0.2 on 2022-10-02 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_cinemahall_movie_moviesession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='row',
            new_name='rows',
        ),
    ]
