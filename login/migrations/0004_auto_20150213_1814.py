# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150213_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='date_of_birth',
            field=models.DateField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name=b'first_name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name=b'last_name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name=b'email address', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, help_text=b'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name=b'active'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(help_text=b'Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=30, verbose_name=b'username'),
            preserve_default=True,
        ),
    ]
