# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-17 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_setting', '0001_initial'),
        ('aboutothers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aoquestion',
            name='PageSetting',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='page_setting.PageSetting'),
        ),
    ]
