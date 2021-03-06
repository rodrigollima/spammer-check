# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=256)),
                ('subject', models.CharField(max_length=256)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('authorize', models.BooleanField(default=False)),
                ('hash', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
