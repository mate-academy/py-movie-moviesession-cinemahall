# Generated by Django 4.0.2 on 2023-11-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('actors', models.ManyToManyField(related_name='actors', to='db.Actor')),
                ('genres', models.ManyToManyField(related_name='genres', to='db.Genre')),
            ],
        ),
    ]
