# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0008_employment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(verbose_name='advisor n', max_length=64, help_text="Please enter advisor's name", unique=True)),
            ],
            options={
                'verbose_name': 'Advisor',
                'verbose_name_plural': 'Advisors',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='education',
            name='advisor',
            field=models.ForeignKey(null=True, help_text="Please specify advisor's name", blank=True, to='lab_members.Advisor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employment',
            name='advisor',
            field=models.ForeignKey(null=True, help_text="Please specify advisor's name", blank=True, to='lab_members.Advisor'),
            preserve_default=True,
        ),
    ]
