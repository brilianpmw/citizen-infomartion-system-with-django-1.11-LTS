# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-24 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0011_tambahpengumuman_deskripsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokumentasi',
            name='gambar1',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='dokumentasi',
            name='gambar2',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='dokumentasi',
            name='gambar3',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='dokumentasi',
            name='gambar4',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='dokumentasi',
            name='gambar5',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='dokumentasi',
            name='gambarutama',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
