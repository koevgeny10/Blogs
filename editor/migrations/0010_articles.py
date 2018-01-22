# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bloging', '0007_auto_20180122_1801'),
        ('editor', '0009_auto_20180118_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('text', models.TextField(null=True)),
                ('likes', models.BigIntegerField(default=0)),
                ('dislikes', models.BigIntegerField(default=0)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloging.Blogs', to_field='name')),
            ],
        ),
    ]
