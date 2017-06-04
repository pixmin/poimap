# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poimap', '0018_auto_20170516_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='depth',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poi',
            name='numchild',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poi',
            name='path',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]