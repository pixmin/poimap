# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-04 15:11
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0028_auto_20170604_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(dim=3, geography=True, srid=4326),
        ),
    ]
