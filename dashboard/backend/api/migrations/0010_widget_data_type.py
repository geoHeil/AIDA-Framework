# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-24 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180712_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='data_type',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
