# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0006_song_pace'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='spotifyLink',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='song_album',
            name='album',
            field=models.ForeignKey(related_name='songs', to='audio.Album'),
        ),
        migrations.AlterField(
            model_name='song_album',
            name='song',
            field=models.ForeignKey(related_name='albums', to='audio.Song'),
        ),
    ]
