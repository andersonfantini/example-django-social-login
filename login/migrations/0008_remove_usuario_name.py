# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_usuario_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='name',
        ),
    ]
