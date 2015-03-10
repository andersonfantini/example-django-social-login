# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20150217_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='birthday',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(db_index=True, unique=True, max_length=255, verbose_name=b'e-mail', error_messages={b'unique': 'J\xe1 existe cadastro com este e-mail. Caso perdeu sua senha, use o esqueci minha senha na tela inicial'}),
            preserve_default=True,
        ),
    ]
