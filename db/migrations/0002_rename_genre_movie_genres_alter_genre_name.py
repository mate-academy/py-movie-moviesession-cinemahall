
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='genres',
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
