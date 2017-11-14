# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0003_auto_20171114_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notify',
            name='hash',
        ),
        migrations.AlterField(
            model_name='notify',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]