# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_path', models.CharField(max_length=255, verbose_name='\u041f\u0443\u0442\u044c \u043a \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u043c\u0443 \u0444\u0430\u0439\u043b\u0443')),
                ('destination_path', models.CharField(max_length=255, verbose_name='\u041f\u0443\u0442\u044c \u043a \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0438\u0440\u0443\u044e\u0449\u0435\u043c\u0443 \u0444\u0430\u0439\u043b\u0443')),
                ('url', models.URLField(max_length=511, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043c\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f')),
                ('email', models.EmailField(max_length=254, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f')),
                ('convert', models.OneToOneField(verbose_name='\u0421\u043e\u0431\u044b\u0442\u0438\u0435 \u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0430\u0446\u0438\u0438', to='convert.Convert')),
            ],
        ),
    ]
