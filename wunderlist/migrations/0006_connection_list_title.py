# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wunderlist', '0005_auto_20151226_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='list_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='List Title'),
        ),
    ]