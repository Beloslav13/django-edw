# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-22 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edw', '0018_email_notification_notificationattachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='particularproblem',
            name='state',
        ),
    ]
