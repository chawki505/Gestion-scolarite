# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0007_auto_20180609_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='moyenne1',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='moyenne2',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
