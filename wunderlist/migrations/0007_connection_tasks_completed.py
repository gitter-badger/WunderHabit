# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wunderlist', '0006_connection_list_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='tasks_completed',
            field=models.IntegerField(default=0, verbose_name='tasks_completed'),
        ),
    ]
