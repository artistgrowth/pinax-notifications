# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-16 13:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pinax_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticesetting',
            name='scoping_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='noticesetting',
            name='scoping_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='noticesetting',
            unique_together=set([('user', 'notice_type', 'medium', 'scoping_content_type', 'scoping_object_id')]),
        ),
    ]
