# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('note', models.CharField(max_length=250)),
                ('favourite', models.BooleanField(max_length=250)),
                ('imageurl', models.CharField(max_length=250)),
            ],
        ),
    ]
