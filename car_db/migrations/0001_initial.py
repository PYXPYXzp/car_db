# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-05 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('wire_color', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(editable=False)),
                ('update_date', models.DateTimeField()),
                ('note', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_db.Car')),
            ],
        ),
    ]