# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 19:17
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_db', '0002_auto_20170905_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color',
            field=colorful.fields.RGBColorField(default=1),
            preserve_default=False,
        ),
    ]