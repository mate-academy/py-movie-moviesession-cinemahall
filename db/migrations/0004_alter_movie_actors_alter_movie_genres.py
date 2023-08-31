# Generated by Django 4.0.2 on 2023-08-31 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_rename_movies_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='db.Genre'),
        ),
    ]
