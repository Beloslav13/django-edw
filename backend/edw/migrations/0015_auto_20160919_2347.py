# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-19 20:47
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('edw', '0014_auto_20160919_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='particularproblem',
            name='state',
            field=django_fsm.FSMField(default='new', max_length=50, protected=True, verbose_name='State'),
        ),
    ]