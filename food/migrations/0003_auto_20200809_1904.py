# Generated by Django 3.0.7 on 2020-08-09 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20200809_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='genre',
            new_name='locate',
        ),
    ]
