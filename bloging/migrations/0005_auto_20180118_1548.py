# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloging', '0004_auto_20171231_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
    ]
