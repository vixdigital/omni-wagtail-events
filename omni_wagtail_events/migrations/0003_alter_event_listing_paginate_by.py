# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omni_wagtail_events', '0002_add_event_detail_repeat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendaitems',
            options={},
        ),
        migrations.AlterField(
            model_name='eventlistingpage',
            name='paginate_by',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]