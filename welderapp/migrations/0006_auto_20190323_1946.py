# Generated by Django 2.1.7 on 2019-03-23 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welderapp', '0005_auto_20190322_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='welderitem',
            name='client_name',
        ),
        migrations.RemoveField(
            model_name='welderorder',
            name='user',
        ),
        migrations.DeleteModel(
            name='WelderItem',
        ),
        migrations.DeleteModel(
            name='Welderorder',
        ),
    ]
