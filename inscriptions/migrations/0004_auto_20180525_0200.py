# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0003_auto_20180525_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='date_naissance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='lieu_naissance',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
