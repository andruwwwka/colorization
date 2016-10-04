# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0008_auto_20160112_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='convert_time',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0430\u0446\u0438\u0438'),
        ),
    ]
