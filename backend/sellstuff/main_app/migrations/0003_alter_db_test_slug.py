# Generated by Django 4.2.1 on 2024-05-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_db_test_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_test',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
