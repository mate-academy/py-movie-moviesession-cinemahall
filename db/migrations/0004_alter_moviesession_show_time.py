# Generated by Django 4.0.2 on 2024-01-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_moviesession_show_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='show_time',
            field=models.DateTimeField(),
        ),
    ]
