# Generated by Django 4.0.2 on 2023-03-07 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='row',
            new_name='rows',
        ),
    ]