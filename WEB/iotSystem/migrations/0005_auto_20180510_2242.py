# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-10 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotSystem', '0004_auto_20180507_0023'),
    ]

    operations = [
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AlterField(
            model_name='data',
            name='at',
            field=models.CharField(default='', max_length=20, verbose_name='\u5149\u7167'),
        ),
    ]