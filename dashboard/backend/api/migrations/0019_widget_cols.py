# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_widgetgroup_cols'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='cols',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
