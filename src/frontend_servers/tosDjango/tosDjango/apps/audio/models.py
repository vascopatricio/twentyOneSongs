from django.db import models


# Create your models here.

class Song(models.Model):
    """
    Model for a Song.
    """

    title = models.CharField(max_length=128, default='')

    pace = models.CharField(max_length=16, default='Slow')

    durM = models.IntegerField(default=0)
    durS = models.IntegerField(default=0)

    ytVideoLink = models.CharField(max_length=256, default='', null=True, blank=True)
    ytAudioLink = models.CharField(max_length=256, default='', null=True, blank=True)

    geniusLink = models.CharField(max_length=256, default='', null=True, blank=True)

    spotifyLink = models.CharField(max_length=256, default='', null=True, blank=True)
    appleMusicLink = models.CharField(max_length=256, default='', null=True, blank=True)

    def toJSON(self):
        import simplejson
        return simplejson.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    def __str__(self):
        return self.title

    def getAlbum(self):
        try:
            return (self.albums.all())[0].album
        except:
            pass

    def hasYtLinks(self):
        if self.ytAudioLink or self.ytVideoLink:
            return "Yes"
        return "No"
    hasYtLinks.short_description = 'Has YT Links?'

    def hasGeniusLink(self):
        if self.geniusLink:
            return "Yes"
        return "No"
    hasGeniusLink.short_description = 'Has Genius Links'

    def durationToStr(self):
        return "%02d:%02d" % (self.durM,self.durS)
    durationToStr.short_description = 'Duration'

    def getGenres(self):
        genresToStr = ''
        for genre in [rel.genre for rel in self.genres.all()]:
            genresToStr += str(genre)+', '
        if len(genresToStr):
            genresToStr = genresToStr[0:-2]
        return genresToStr
    getGenres.short_description = 'Genres'

    def getTopics(self):
        topicsToStr = ''
        for genre in [rel.topic for rel in self.topics.all()]:
            topicsToStr += str(genre) + ', '
        if len(topicsToStr):
            topicsToStr = topicsToStr[0:-2]
        return topicsToStr
    getTopics.short_description = 'Topics'



class Album(models.Model):
    """
    Model for a Album.
    """

    title = models.CharField(max_length=128, default='')

    year = models.IntegerField(default=0)

    spotifyLink = models.CharField(max_length=256, default='', null=True, blank=True)
    appleMusicLink = models.CharField(max_length=256, default='', null=True, blank=True)

    thumbUrl =  models.CharField(max_length=256, default='', null=True, blank=True)

    def toJSON(self):
        import simplejson
        return simplejson.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    def __str__(self):
        toStr = self.title
        if self.year > 0:
            toStr += ' (' + str(self.year) + ')'
        return toStr


class Song_Album(models.Model):
    """
    """

    song = models.ForeignKey('audio.Song', related_name='albums')

    album = models.ForeignKey('audio.Album', related_name='songs')

    trackNo = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Song - Album Relationship'
        verbose_name_plural = 'Song - Album Relationships'

    def toJSON(self):
        return {'song_id': self.song_id, 'album_id': self.album_id, 'trackNo': self.trackNo}

    def __str__(self):
        return str(self.song) + ' on ' + str(self.album)
