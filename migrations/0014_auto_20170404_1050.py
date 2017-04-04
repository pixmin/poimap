# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 08:50
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0013_auto_20170404_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='city',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='poi',
            name='country',
            field=django_countries.fields.CountryField(default=b'FR', max_length=2),
        ),
        migrations.AddField(
            model_name='poi',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT(0 0)', srid=4326),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poi',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
