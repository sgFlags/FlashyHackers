# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-01 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_verbose_name_plural_for_calendar'),
        ('MS', '0010_meetinginvitation'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingEventRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Event')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MS.Meeting')),
            ],
        ),
    ]