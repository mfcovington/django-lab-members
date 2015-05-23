# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0018_auto_20150508_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-year_start', '-year_end'], 'verbose_name_plural': 'Education records', 'verbose_name': 'Education record'},
        ),
        migrations.AlterModelOptions(
            name='employment',
            options={'ordering': ['-year_start', '-year_end'], 'verbose_name_plural': 'Employment records', 'verbose_name': 'Employment record'},
        ),
    ]
