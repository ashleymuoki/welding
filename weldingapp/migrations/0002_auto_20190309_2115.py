# Generated by Django 2.1.7 on 2019-03-09 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weldingapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='length',
            new_name='height_feet',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='width',
            new_name='length_feet',
        ),
    ]