# Generated by Django 2.1.7 on 2019-03-17 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welderapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='welderorder',
            old_name='welder',
            new_name='user',
        ),
    ]
