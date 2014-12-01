# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0010_auto_20141130_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='full_name',
            field=models.CharField(max_length=64, verbose_name='advisor name', help_text="Please enter advisor's name", unique=True),
            preserve_default=True,
        ),
    ]
