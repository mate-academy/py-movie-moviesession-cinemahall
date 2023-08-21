# Generated by Django 4.0.2 on 2023-08-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_cinemahall_movie_moviesession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='Movie', to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='Movie', to='db.Genre'),
        ),
    ]