# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 10:46
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('poimap', '0049_auto_20180215_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='poilisting',
            name='extra_placeholder',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname=b'extra_placeholder', to='cms.Placeholder'),
        ),
    ]