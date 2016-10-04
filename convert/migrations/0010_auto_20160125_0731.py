# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0009_auto_20160112_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='convert',
            name='hashed_name',
            field=models.CharField(max_length=511, null=True, verbose_name='\u0425\u044d\u0448 \u0438\u043c\u0435\u043d\u0438 \u0444\u0430\u0439\u043b\u0430'),
        ),
        migrations.AddField(
            model_name='convert',
            name='marked_file',
            field=models.FileField(upload_to=b'static/upload_images/marked/%Y/%m/%d', null=True, verbose_name='\u041f\u0443\u0442\u044c \u043a \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u043c\u0443 \u0444\u0430\u0439\u043b\u0443'),
        ),
        migrations.AlterField(
            model_name='convert',
            name='destination_file',
            field=models.FileField(upload_to=b'static/upload_images/result/%Y/%m/%d', verbose_name='\u041f\u0443\u0442\u044c \u043a \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0438\u0440\u0443\u044e\u0449\u0435\u043c\u0443 \u0444\u0430\u0439\u043b\u0443'),
        ),
        migrations.AlterField(
            model_name='convert',
            name='source_file',
            field=models.FileField(upload_to=b'static/upload_images/source/%Y/%m/%d', verbose_name='\u041f\u0443\u0442\u044c \u043a \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u043c\u0443 \u0444\u0430\u0439\u043b\u0443'),
        ),
    ]
