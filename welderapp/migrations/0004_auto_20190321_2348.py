# Generated by Django 2.1.7 on 2019-03-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welderapp', '0003_auto_20190321_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welderorder',
            name='date_of_completion',
            field=models.DateTimeField(),
        ),
    ]
