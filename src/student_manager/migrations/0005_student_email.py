# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-29 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_manager', '0004_auto_20180629_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
