# Generated by Django 4.0.2 on 2024-03-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='show_time',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]