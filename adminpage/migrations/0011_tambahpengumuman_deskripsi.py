# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-24 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0010_auto_20190624_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='tambahpengumuman',
            name='deskripsi',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
