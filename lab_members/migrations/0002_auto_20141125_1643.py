# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientist',
            name='personal_interests',
            field=models.TextField(blank=True, default='', verbose_name='personal interests', help_text='Please write a personal interests blurb for this scientist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scientist',
            name='research_interests',
            field=models.TextField(blank=True, default='', verbose_name='research interests', help_text='Please write a research interests blurb for this scientist'),
            preserve_default=True,
        ),
    ]
