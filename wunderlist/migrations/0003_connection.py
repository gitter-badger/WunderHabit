# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 16:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wunderlist', '0002_auto_20151223_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_list', models.CharField(max_length=255, verbose_name='List')),
                ('habit', models.CharField(default=b'productivity', max_length=255, verbose_name='Habit')),
                ('token', models.CharField(default='1pekeilAf1C41RACQK2LTp2yuDuqTXDZ', max_length=255, verbose_name='Token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]