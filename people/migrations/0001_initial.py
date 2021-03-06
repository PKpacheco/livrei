# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'nome')),
                ('image', models.ImageField(upload_to=b'people/', verbose_name=b'imagem')),
                ('email', models.EmailField(max_length=255, verbose_name=b'email')),
                ('description', models.CharField(max_length=255, verbose_name=b'descri\xc3\xa7\xc3\xa3o')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'membro',
                'verbose_name_plural': 'membros',
            },
        ),
    ]
