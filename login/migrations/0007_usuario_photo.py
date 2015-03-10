# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20150213_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='photo',
            field=models.CharField(max_length=200, verbose_name=b'photo', blank=True),
            preserve_default=True,
        ),
    ]
