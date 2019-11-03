# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-11-02 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_commoditydetailimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommodityDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Commodity')),
                ('custom_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.CustomAttribute')),
                ('default_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.CommodityAttribute')),
                ('detail_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.CommodityDetailImg')),
            ],
            options={
                'verbose_name_plural': '商品详情',
            },
        ),
    ]
