# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20150214_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_name',
        ),
        migrations.AddField(
            model_name='usuario',
            name='birthday',
            field=models.DateField(max_length=200, null=True, verbose_name=b'user_birthday', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='typeaccount',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name=b'e-mail', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'active'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='photo',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
