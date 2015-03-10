# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20150213_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date_of_birth',
            field=models.CharField(max_length=200, verbose_name=b'user_birthday', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=None, max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
