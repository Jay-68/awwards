# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-25 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0009_auto_20191125_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
