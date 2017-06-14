# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import elasticsearch_django.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
            ],
            bases=(models.Model, elasticsearch_django.models.SearchDocumentMixin),
        ),
    ]
