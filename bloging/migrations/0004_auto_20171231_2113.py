# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloging', '0003_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]