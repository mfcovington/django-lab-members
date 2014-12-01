# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0004_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(help_text='Please enter a field of study', unique=True, verbose_name='field of study', max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Fields',
                'verbose_name': 'Field',
            },
            bases=(models.Model,),
        ),
    ]
