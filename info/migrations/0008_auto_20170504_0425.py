# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20170419_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allow',
            name='allowedUserProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowedUserProfile', to='info.Userprofile'),
        ),
        migrations.AlterField(
            model_name='allow',
            name='allowingUserProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowingUserProfile', to='info.Userprofile'),
        ),
        migrations.AlterField(
            model_name='wdt',
            name='wdtUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Userprofile'),
        ),
    ]
