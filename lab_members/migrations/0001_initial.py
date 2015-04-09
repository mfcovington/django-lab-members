# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, help_text='Please enter a title for this position', default='', verbose_name='title')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scientist',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=64, unique=True, help_text='Please enter a full name for this scientist', default='', verbose_name='full name')),
                ('slug', models.SlugField(max_length=64, help_text='Please enter a unique slug for this scientist', default='', verbose_name='slug')),
                ('title', models.ForeignKey(blank=True, help_text='Please specify a title for this scientist', default=None, to='lab_members.Position', null=True)),
            ],
            options={
                'verbose_name': 'Scientist',
                'verbose_name_plural': 'Scientists',
            },
            bases=(models.Model,),
        ),
    ]
