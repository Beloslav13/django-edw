# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-22 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('post_office', '0010_auto_20160820_0052'),
        ('filer', '0006_auto_20160623_1627'),
        ('edw', '0017_particularproblem_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('transition_target', models.CharField(max_length=50, verbose_name='Event')),
                ('mail_to', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Mail to')),
                ('mail_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_office.EmailTemplate', verbose_name='Template')),
            ],
            options={
                'ordering': ('transition_target', 'mail_to'),
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='NotificationAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email_attachment', to='filer.File')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edw.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('post_office.email',),
        ),
    ]
