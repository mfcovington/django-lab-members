# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('lab_members', '0016_auto_20141204_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientist',
            name='photo',
            field=filer.fields.image.FilerImageField(blank=True, help_text='Please upload an photo of this scientist', null=True, to='filer.Image'),
            preserve_default=True,
        ),
    ]
