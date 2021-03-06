# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_auto_20170327_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postprofile',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='postprofile',
            name='post1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='practice.Post1'),
        ),
        migrations.AlterField(
            model_name='postprofile',
            name='post2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='practice.Post2'),
        ),
    ]
