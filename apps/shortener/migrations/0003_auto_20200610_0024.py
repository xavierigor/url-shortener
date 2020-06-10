# Generated by Django 3.0.7 on 2020-06-10 00:24

import apps.shortener.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20200609_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short',
            field=models.URLField(default=apps.shortener.models.unique_short_url, unique=True),
        ),
    ]
