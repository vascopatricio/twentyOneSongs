# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song_Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='title',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='song_album',
            name='album',
            field=models.ForeignKey(related_name='Songs', to='audio.Album'),
        ),
        migrations.AddField(
            model_name='song_album',
            name='song',
            field=models.ForeignKey(related_name='Albums', to='audio.Song'),
        ),
    ]
