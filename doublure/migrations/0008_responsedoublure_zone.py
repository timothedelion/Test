# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doublure', '0007_auto_20170731_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsedoublure',
            name='zone',
            field=models.CharField(choices=[('O', 'Ouest'), ('S', 'Sud'), ('E', 'Est')], default='O', max_length=200),
        ),
    ]
