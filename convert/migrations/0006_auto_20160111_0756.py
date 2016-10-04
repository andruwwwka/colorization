# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0005_auto_20160111_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convert',
            name='convert_time',
        ),
        migrations.AddField(
            model_name='convert',
            name='convert_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 11, 7, 56, 51, 70070, tzinfo=utc), verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0430\u0446\u0438\u0438'),
        ),
    ]
