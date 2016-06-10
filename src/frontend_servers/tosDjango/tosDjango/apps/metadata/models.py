from django.db import models


class Topic(models.Model):
    """
    """

    name = models.CharField(max_length=32, default='')

    def toJSON(self):
        import simplejson
        return simplejson.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    def getSongCount(self):
        return len(self.songs.all())

    getSongCount.short_description = 'Song Count'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    """

    name = models.CharField(max_length=32, default='')

    def toJSON(self):
        import simplejson
        return simplejson.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    def getSongCount(self):
        return len(self.songs.all())

    getSongCount.short_description = 'Song Count'

    def __str__(self):
        return self.name


class Song_Topic(models.Model):
    """
    """

    song = models.ForeignKey('audio.Song', related_name='topics')

    topic = models.ForeignKey('metadata.Topic', related_name='songs')

    def __str__(self):
        return str(self.song) + ' - ' + str(self.topic)

    def toJSON(self):
        return {'song_id': self.song_id, 'topic_id': self.topic_id}

    class Meta:
        verbose_name = 'Song - Topic Relation'
        verbose_name_plural = 'Song - Topic Relations'


class Song_Genre(models.Model):
    """
    """

    song = models.ForeignKey('audio.Song', related_name='genres')

    genre = models.ForeignKey('metadata.Genre', related_name='songs')

    def toJSON(self):
        return {'song_id': self.song_id, 'genre_id': self.genre_id}

    def __str__(self):
        return str(self.song) + ' - ' + str(self.genre)

    class Meta:
        verbose_name = 'Song - Genre Relation'
        verbose_name_plural = 'Song - Genre Relations'
