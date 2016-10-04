# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0011_auto_20160127_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='sended',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0438\u0441\u044c\u043c\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e'),
        ),
    ]
