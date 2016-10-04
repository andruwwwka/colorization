# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0003_auto_20151230_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='convert_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 30, 12, 13, 29, 534933, tzinfo=utc), verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='convert',
            name='destination_file',
            field=models.FileField(upload_to=b'static/upload_images/%Y/%m/%d', verbose_name='\u041f\u0443\u0442\u044c \u043a \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0438\u0440\u0443\u044e\u0449\u0435\u043c\u0443 \u0444\u0430\u0439\u043b\u0443'),
        ),
        migrations.AlterField(
            model_name='convert',
            name='source_file',
            field=models.FileField(upload_to=b'static/upload_images/%Y/%m/%d', verbose_name='\u041f\u0443\u0442\u044c \u043a \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u043c\u0443 \u0444\u0430\u0439\u043b\u0443'),
        ),
    ]
