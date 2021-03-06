# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'nome')),
                ('description', models.CharField(max_length=255, verbose_name=b'descri\xc3\xa7\xc3\xa3o')),
                ('ddd', models.CharField(max_length=2, verbose_name=b'DDD')),
                ('telephone', models.CharField(max_length=9, verbose_name=b'telefone')),
                ('email', models.EmailField(max_length=255, verbose_name=b'email')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Institui\xe7\xe3o',
                'verbose_name_plural': 'Institui\xe7\xf5es',
            },
        ),
    ]
