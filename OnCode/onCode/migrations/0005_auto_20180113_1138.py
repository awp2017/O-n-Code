# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onCode', '0004_auto_20180113_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='university',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
