# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-10 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20170510_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
