# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'people/', verbose_name=b'imagem'),
        ),
    ]
