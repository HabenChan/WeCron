# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-27 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remind', '0007_auto_20170813_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='remind',
            name='external_url',
            field=models.URLField(blank=True, max_length=120, null=True, verbose_name='\u5916\u90e8\u94fe\u63a5\u5730\u5740'),
        ),
    ]