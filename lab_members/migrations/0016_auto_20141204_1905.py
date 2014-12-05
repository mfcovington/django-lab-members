# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0015_scientist_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientist',
            name='alumni_redirect_url',
            field=models.URLField(help_text="If former lab member, please enter the scientist's new URL", blank=True, null=True, verbose_name='alumni redirect URL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scientist',
            name='current',
            field=models.BooleanField(help_text='Please specify whether scientist is a current lab member', verbose_name='current lab member', default=True),
            preserve_default=True,
        ),
    ]
