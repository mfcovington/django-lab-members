# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0013_advisor_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advisor',
            options={'verbose_name': 'Advisor', 'verbose_name_plural': 'Advisors', 'ordering': ['full_name']},
        ),
        migrations.AlterModelOptions(
            name='degree',
            options={'verbose_name': 'Degree', 'verbose_name_plural': 'Degrees', 'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'Educational record', 'verbose_name_plural': 'Educational records', 'ordering': ['-year_start', '-year_end']},
        ),
        migrations.AlterModelOptions(
            name='employment',
            options={'verbose_name': 'Employmental record', 'verbose_name_plural': 'Employmental records', 'ordering': ['-year_start', '-year_end']},
        ),
        migrations.AlterModelOptions(
            name='field',
            options={'verbose_name': 'Field', 'verbose_name_plural': 'Fields', 'ordering': ['label']},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'verbose_name': 'Institution', 'verbose_name_plural': 'Institutions', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Position', 'verbose_name_plural': 'Positions', 'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='scientist',
            options={'verbose_name': 'Scientist', 'verbose_name_plural': 'Scientists', 'ordering': ['full_name']},
        ),
    ]
