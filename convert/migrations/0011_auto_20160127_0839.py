# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0010_auto_20160125_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='convert',
        ),
        migrations.AddField(
            model_name='convert',
            name='sended',
            field=models.NullBooleanField(default=None, verbose_name='\u041f\u0438\u0441\u044c\u043c\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e'),
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
