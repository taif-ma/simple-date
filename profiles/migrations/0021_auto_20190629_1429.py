# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-29 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_auto_20190628_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='citylat',
            new_name='citylat',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='citylong',
            new_name='citylong',
        ),
    ]
