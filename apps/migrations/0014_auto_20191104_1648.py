# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-11-04 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_auto_20191104_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintoken',
            name='addtime',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
