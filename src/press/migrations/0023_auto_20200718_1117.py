# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-18 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0022_press_disable_journals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='press',
            name='theme',
            field=models.CharField(default='OLH', max_length=255),
        ),
    ]