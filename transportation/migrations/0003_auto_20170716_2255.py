# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 22:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0002_auto_20170716_2247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LineStop',
            new_name='RouteStop',
        ),
    ]
