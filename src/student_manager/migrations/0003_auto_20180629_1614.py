# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-29 10:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_manager', '0002_auto_20180629_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 16, 14, 34, 611013)),
        ),
        migrations.AlterField(
            model_name='student',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 16, 14, 34, 611013)),
        ),
    ]