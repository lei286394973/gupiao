# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('article_type', models.IntegerField(default=1, choices=[(1, b'A\xe8\x82\xa1')])),
                ('from_url', models.CharField(unique=True, max_length=128)),
                ('img', models.CharField(max_length=128, null=True, blank=True)),
                ('sort_num', models.IntegerField(default=0, db_index=True)),
                ('state', models.BooleanField(default=True, db_index=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, db_index=True)),
            ],
            options={
                'ordering': ['-sort_num', '-create_time'],
            },
        ),
    ]
