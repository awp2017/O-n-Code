# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 14:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('onCode', '0005_auto_20180113_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResolvedProblems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onCode.Problem')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='resolvedproblems',
            unique_together=set([('problem_id', 'user_id')]),
        ),
    ]