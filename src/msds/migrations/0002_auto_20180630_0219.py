# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 08:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msds', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msdsobject',
            options={'ordering': ('pk',), 'permissions': (('view_msdsobject', 'Can see available MSDSObject'),)},
        ),
    ]
