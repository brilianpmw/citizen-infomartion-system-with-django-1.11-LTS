# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-23 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0006_auto_20190623_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tambahpengumuman',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
