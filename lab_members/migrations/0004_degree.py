# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0003_institution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='degree title', help_text='Please enter a degree type', unique=True, max_length=64)),
            ],
            options={
                'verbose_name': 'Degree',
                'verbose_name_plural': 'Degrees',
            },
            bases=(models.Model,),
        ),
    ]
