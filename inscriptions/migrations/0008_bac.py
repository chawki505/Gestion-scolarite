# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 21:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0007_auto_20180526_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100)),
                ('note', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('mention', models.CharField(choices=[('sans mention', 'Bac sans mention : entre 10 et 12/20'), ('mention assez bien', 'Bac avec mention assez bien : entre 12 et 14/20'), ('mention bien', 'Bac avec mention bien : entre 14 et 16/20'), ('mention très bien', 'Bac avec mention très bien : 16/20 et plus')], max_length=100)),
                ('session', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=2018)),
                ('etudiant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inscriptions.Etudiant')),
            ],
        ),
    ]
