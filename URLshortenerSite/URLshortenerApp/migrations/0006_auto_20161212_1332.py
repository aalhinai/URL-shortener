# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 13:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('URLshortenerApp', '0005_auto_20161211_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usr_urls',
            options={'verbose_name': 'Total URLs', 'verbose_name_plural': 'Total URLs'},
        ),
    ]
