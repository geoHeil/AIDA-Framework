# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20181105_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetgroup',
            name='cols',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
