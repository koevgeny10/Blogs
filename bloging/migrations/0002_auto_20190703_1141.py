# Generated by Django 2.2 on 2019-07-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='moment',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='moment',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
