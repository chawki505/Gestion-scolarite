# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annee_universitaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Annee_universitaire',
                'verbose_name_plural': 'Annees_universitaire',
                'db_table': 'annee_universitaire',
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Departement',
                'verbose_name_plural': 'Departements',
                'db_table': 'departement',
            },
        ),
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Domaine',
                'verbose_name_plural': 'Domaines',
                'db_table': 'domaine',
            },
        ),
        migrations.CreateModel(
            name='Etablisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Etablisement',
                'verbose_name_plural': 'Etablisements',
                'db_table': 'etablisement',
            },
        ),
        migrations.CreateModel(
            name='Faculte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=256)),
                ('etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissements.Etablisement')),
            ],
            options={
                'verbose_name': 'Faculte',
                'verbose_name_plural': 'Facultes',
                'db_table': 'faculte',
            },
        ),
        migrations.AddField(
            model_name='domaine',
            name='faculte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissements.Faculte'),
        ),
        migrations.AddField(
            model_name='departement',
            name='domaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissements.Domaine'),
        ),
    ]
