# Generated by Django 4.0.2 on 2022-06-20 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemahall',
            name='rows',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cinemahall',
            name='seats_in_row',
            field=models.IntegerField(default=1),
        ),
    ]
