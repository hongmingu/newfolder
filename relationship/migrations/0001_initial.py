# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 19:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('title', '0002_title_titleuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=200)),
                ('title', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='title.Title')),
            ],
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content_Flowed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_is_Flowed', to='relationship.ContentRelationship')),
            ],
        ),
        migrations.CreateModel(
            name='Title2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleText', models.TextField(max_length=160, unique=True)),
                ('titleCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('titleUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionpro', models.TextField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='flow',
            name='user_Flowing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_is_Flowing', to='relationship.UserRelationship'),
        ),
        migrations.AddField(
            model_name='contentrelationship',
            name='title2',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relationship.Title2'),
        ),
        migrations.AddField(
            model_name='bridge',
            name='user_Bridged',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_is_bridged', to='relationship.UserRelationship'),
        ),
        migrations.AddField(
            model_name='bridge',
            name='user_Bridging',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_is_bridging', to='relationship.UserRelationship'),
        ),
        migrations.AlterUniqueTogether(
            name='flow',
            unique_together=set([('user_Flowing', 'content_Flowed')]),
        ),
        migrations.AlterUniqueTogether(
            name='bridge',
            unique_together=set([('user_Bridging', 'user_Bridged')]),
        ),
    ]