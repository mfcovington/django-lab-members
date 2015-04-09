# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0014_auto_20141202_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientist',
            name='current',
            field=models.BooleanField(verbose_name='current lab member', default=True, help_text='Specify whether scientist is a current lab member'),
            preserve_default=True,
        ),
    ]
