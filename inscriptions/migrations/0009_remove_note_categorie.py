# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0008_auto_20180609_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='categorie',
        ),
    ]