# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0002_auto_20151229_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='convert',
            old_name='destination_path',
            new_name='destination_file',
        ),
        migrations.RenameField(
            model_name='convert',
            old_name='source_path',
            new_name='source_file',
        ),
        migrations.AlterField(
            model_name='convert',
            name='convert_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 30, 11, 26, 26, 256347, tzinfo=utc), verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0430\u0446\u0438\u0438'),
        ),
    ]
