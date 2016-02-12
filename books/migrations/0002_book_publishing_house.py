# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 18:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publishing_house',
            field=models.CharField(default=datetime.datetime(2016, 2, 12, 18, 13, 43, 904130, tzinfo=utc), max_length=255, verbose_name='Editora'),
            preserve_default=False,
        ),
    ]
