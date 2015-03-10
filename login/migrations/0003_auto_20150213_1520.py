# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_usuario_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nome',
            new_name='username',
        ),
    ]
