# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-02 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bac',
            name='mention',
            field=models.CharField(choices=[('sans mention', 'Bac sans mention : entre 10 et 12/20'), ('mention assez bien', 'Bac avec mention assez bien : entre 12 et 14/20'), ('mention bien', 'Bac avec mention bien : entre 14 et 16/20'), ('mention très bien', 'Bac avec mention très bien : 16/20 et plus')], default=('sans mention', 'Bac sans mention : entre 10 et 12/20'), max_length=256),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='adresse',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='nationalite',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='sexe',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=256),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='telephone',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='categorie',
            field=models.CharField(blank=True, choices=[('Inscription', 'Inscription'), ('Reinscription', 'Reinscription')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='categorie',
            field=models.CharField(choices=[('CC', 'CC'), ('EF', 'EF'), ('ER', 'ER')], max_length=256),
        ),
        migrations.AlterField(
            model_name='note',
            name='inscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='inscriptions.Inscription'),
        ),
    ]