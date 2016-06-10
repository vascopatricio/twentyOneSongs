# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_auto_20160610_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song_album',
            options={'verbose_name': 'Song - Album Relationship', 'verbose_name_plural': 'Song - Album Relationships'},
        ),
        migrations.AddField(
            model_name='song',
            name='geniusLink',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AddField(
            model_name='song',
            name='ytAudioLink',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AddField(
            model_name='song',
            name='ytVideoLink',
            field=models.CharField(default=b'', max_length=256),
        ),
    ]
