# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-11-02 09:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_auto_20191102_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodityattribute',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='commoditydetail',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='commoditydetailimg',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='customattribute',
            name='commodity',
        ),
        migrations.DeleteModel(
            name='CommodityAttribute',
        ),
        migrations.DeleteModel(
            name='CommodityDetail',
        ),
        migrations.DeleteModel(
            name='CommodityDetailImg',
        ),
        migrations.DeleteModel(
            name='CustomAttribute',
        ),
    ]
