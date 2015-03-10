# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20150213_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='date_of_birth',
            field=models.CharField(max_length=200, null=True, verbose_name=b'user_birthday', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=100, verbose_name=b'username'),
            preserve_default=True,
        ),
    ]
