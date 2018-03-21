# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 09:18
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0052_poi_extra_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='extra_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
    ]