# Generated by Django 3.0.7 on 2020-06-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='full',
            field=models.URLField(max_length=500, verbose_name='full url'),
        ),
    ]
