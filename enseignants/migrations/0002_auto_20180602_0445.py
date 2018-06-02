# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-02 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enseignants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='adresse',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='nationalite',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='telephone',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
