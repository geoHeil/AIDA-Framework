# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_widget_cols'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='cols',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='widgetgroup',
            name='cols',
            field=models.IntegerField(default=12),
        ),
    ]
