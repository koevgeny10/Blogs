# Generated by Django 3.0.7 on 2020-06-13 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(error_messages={'unique': 'NOT UNIQUE'}, unique=True)),
                ('picture', models.ImageField(default='/default/blogs_main_image/859_big.jpg', upload_to='blogs_picture/%Y/%m/%d/')),
                ('about', models.TextField(null=True)),
                ('moment', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', related_query_name='blog', to='profile.Profile')),
            ],
            options={
                'ordering': ['moment'],
                'get_latest_by': 'moment',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moment', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', related_query_name='subscriber', to='blogs.Blog')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribes', related_query_name='subscribe', to='profile.Profile')),
            ],
            options={
                'ordering': ['moment'],
                'get_latest_by': 'moment',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='subscribe',
            field=models.ManyToManyField(related_name='a', through='blogs.Subscribe', to='profile.Profile'),
        ),
    ]
