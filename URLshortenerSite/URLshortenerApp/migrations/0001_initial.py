# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usr_Urls',
            fields=[
                ('short_id', models.SlugField(max_length=8, primary_key=True, serialize=False)),
                ('httpurl', models.URLField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(default='User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
