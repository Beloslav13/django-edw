# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-12 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edw', '0058_auto_20161211_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]