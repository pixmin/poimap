# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-14 20:10
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0028_ticket_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='connections',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
    ]
