# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 16:05
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0005_auto_20180119_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='name',
            field=models.CharField(default='test', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default='test', editable=False, populate_from='name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='direction',
            field=models.CharField(choices=[('1', 'Aller'), ('2', 'Retour')], default='1', max_length=1),
        ),
    ]
