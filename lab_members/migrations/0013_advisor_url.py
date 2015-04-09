# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0012_scientist_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisor',
            name='url',
            field=models.URLField(help_text="Please enter advisor's website", null=True, blank=True, verbose_name='advisor website'),
            preserve_default=True,
        ),
    ]
