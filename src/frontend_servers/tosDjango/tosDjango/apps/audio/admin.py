from django.contrib import admin

# Register your models here.

# Create your models here.
from tosDjango.apps.audio.models import *


class SongAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('title', 'durationToStr', 'getAlbum', 'pace', 'hasYtLinks', 'hasGeniusLink', 'getGenres', 'getTopics')


class AlbumAdmin(admin.ModelAdmin):
    """
    """

    pass


class Song_AlbumAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('album', 'song', 'trackNo')


admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song_Album, Song_AlbumAdmin)
