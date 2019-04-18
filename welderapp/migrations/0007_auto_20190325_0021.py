# Generated by Django 2.1.7 on 2019-03-24 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('welderapp', '0006_auto_20190323_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('cost', models.IntegerField()),
                ('picture', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Welder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welder_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('cover', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='design',
            name='welder_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='welderapp.Welder'),
        ),
    ]
