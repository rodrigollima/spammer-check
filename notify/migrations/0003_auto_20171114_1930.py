# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0002_notify_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='subject',
            field=models.TextField(),
        ),
    ]
