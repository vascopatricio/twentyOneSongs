# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0005_auto_20160610_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='pace',
            field=models.CharField(default=b'Slow', max_length=16),
        ),
    ]
