# Generated by Django 4.0.2 on 2023-11-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_moviesession_show_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='db.Genre'),
        ),
    ]
