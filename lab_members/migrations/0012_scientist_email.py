# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0011_auto_20141130_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientist',
            name='email',
            field=models.EmailField(help_text='Please enter email address', max_length=75, null=True, verbose_name='email address'),
            preserve_default=True,
        ),
    ]
