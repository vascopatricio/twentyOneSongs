# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0003_auto_20160610_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='name',
            field=models.CharField(default=b'', max_length=32),
        ),
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default=b'', max_length=32),
        ),
    ]
