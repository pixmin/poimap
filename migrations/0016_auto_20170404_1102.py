# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0015_poi_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poiaddress',
            name='poi',
        ),
        migrations.DeleteModel(
            name='POIAddress',
        ),
    ]
