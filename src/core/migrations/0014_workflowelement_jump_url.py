# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-09 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180207_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflowelement',
            name='jump_url',
            field=models.CharField(default='core_dashboard', max_length=255),
            preserve_default=False,
        ),
    ]