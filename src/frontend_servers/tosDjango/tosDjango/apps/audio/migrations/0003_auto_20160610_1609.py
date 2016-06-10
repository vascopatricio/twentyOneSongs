# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_auto_20160610_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='durM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='durS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song_album',
            name='trackNo',
            field=models.IntegerField(default=0),
        ),
    ]
