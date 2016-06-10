# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_auto_20160610_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='geniusLink',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='ytAudioLink',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='ytVideoLink',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
    ]
