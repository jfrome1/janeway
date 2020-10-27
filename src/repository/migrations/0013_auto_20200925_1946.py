# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-25 19:46
from __future__ import unicode_literals

import core.file_system
from django.db import migrations, models
import repository.models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0012_auto_20200925_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='favicon',
            field=models.ImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(location='/vol/janeway/src/media'), upload_to=repository.models.repo_media_upload),
        ),
        migrations.AddField(
            model_name='repository',
            name='hero_background',
            field=models.ImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(location='/vol/janeway/src/media'), upload_to=repository.models.repo_media_upload),
        ),
    ]