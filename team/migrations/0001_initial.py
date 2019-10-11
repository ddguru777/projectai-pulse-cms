# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-10 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organization.Organization')),
            ],
        ),
    ]
