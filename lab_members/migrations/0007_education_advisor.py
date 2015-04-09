# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0006_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='advisor',
            field=models.CharField(blank=True, verbose_name='advisor', max_length=64, help_text="Please enter advisor's name", null=True),
            preserve_default=True,
        ),
    ]
