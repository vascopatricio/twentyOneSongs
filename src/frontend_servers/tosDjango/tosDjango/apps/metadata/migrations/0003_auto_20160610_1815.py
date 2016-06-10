# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0006_song_pace'),
        ('metadata', '0002_auto_20160610_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='song_genre',
            name='song',
            field=models.ForeignKey(related_name='genres', default=None, to='audio.Song'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song_topic',
            name='song',
            field=models.ForeignKey(related_name='topics', default=None, to='audio.Song'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song_genre',
            name='genre',
            field=models.ForeignKey(related_name='songs', default=None, to='metadata.Genre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song_topic',
            name='topic',
            field=models.ForeignKey(related_name='songs', default=None, to='metadata.Topic'),
            preserve_default=False,
        ),
    ]
