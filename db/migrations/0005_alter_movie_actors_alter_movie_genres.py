# Generated by Django 4.0.2 on 2023-05-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_moviesession'),
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
