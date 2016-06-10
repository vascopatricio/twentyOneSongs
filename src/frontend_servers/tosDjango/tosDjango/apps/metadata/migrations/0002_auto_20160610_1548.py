# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song_genre',
            options={'verbose_name': 'Song - Genre Relation', 'verbose_name_plural': 'Song - Genre Relations'},
        ),
        migrations.AlterModelOptions(
            name='song_topic',
            options={'verbose_name': 'Song - Topic Relation', 'verbose_name_plural': 'Song - Topic Relations'},
        ),
    ]
