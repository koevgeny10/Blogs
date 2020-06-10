<<<<<<< HEAD:bloging/migrations/0006_articles.py
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloging', '0005_auto_20180118_1548'),
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
=======
# Generated by Django 2.2 on 2019-07-03 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bloging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('name', models.TextField(help_text='please be short', primary_key=True, serialize=False)),
                ('text', models.TextField(null=True)),
                ('likes', models.BigIntegerField(default=0)),
                ('dislikes', models.BigIntegerField(default=0)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', related_query_name='article', to='bloging.Blogs')),
            ],
        ),
    ]
>>>>>>> dev:editor/migrations/0001_initial.py
