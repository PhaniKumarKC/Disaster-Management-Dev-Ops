# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etv', '0007_auto_20190413_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volcaniceruption',
            name='spread_area',
            field=models.PositiveIntegerField(),
        ),
    ]