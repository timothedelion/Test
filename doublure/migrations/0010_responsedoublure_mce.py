# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doublure', '0009_objectifdoublure_seuil_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsedoublure',
            name='mce',
            field=models.CharField(default='MCE', max_length=3),
        ),
    ]