# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0007_auto_20160610_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='appleMusicLink',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='spotifyLink',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='appleMusicLink',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
    ]
