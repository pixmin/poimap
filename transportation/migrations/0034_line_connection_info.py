# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-29 13:16
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0033_bus_equipments'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='connection_info',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
