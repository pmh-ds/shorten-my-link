# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-14 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170830_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='id',
            field=models.SlugField(default='zehn5HMA', primary_key=True, serialize=False),
        ),
    ]
