# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-02 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enseignants', '0002_auto_20180602_0445'),
        ('modules', '0002_auto_20180602_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='unite',
            name='enseignant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsable_unite', to='enseignants.Enseignant'),
        ),
        migrations.AlterField(
            model_name='module',
            name='enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsable_module', to='enseignants.Enseignant'),
        ),
    ]