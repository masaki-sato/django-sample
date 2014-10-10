# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u30d6\u30ed\u30b0\u540d')),
                ('description', models.TextField(max_length=1024, verbose_name='\u8aac\u660e', blank=True)),
                ('header', models.TextField(max_length=1024, verbose_name='\u30d8\u30c3\u30c0\u30fc', blank=True)),
                ('footer', models.TextField(max_length=1024, verbose_name='\u30d5\u30c3\u30bf\u30fc', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
                'verbose_name': '\u30d6\u30ed\u30b0',
                'verbose_name_plural': '\u30d6\u30ed\u30b0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u30bf\u30a4\u30c8\u30eb')),
                ('contents', models.TextField(verbose_name='\u30b3\u30f3\u30c6\u30f3\u30c4')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
                ('blog', models.ForeignKey(to='cms.Blog')),
            ],
            options={
                'ordering': ['-updated_at'],
                'verbose_name': '\u6295\u7a3f',
                'verbose_name_plural': '\u6295\u7a3f',
            },
            bases=(models.Model,),
        ),
    ]
