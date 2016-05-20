# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Vinyl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
    ]
