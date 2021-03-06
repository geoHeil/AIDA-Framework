# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('data', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Dataset',
        ),
    ]
