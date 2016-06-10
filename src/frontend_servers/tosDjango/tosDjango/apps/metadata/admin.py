from django.contrib import admin

# Register your models here.

# Create your models here.
from tosDjango.apps.metadata.models import *


class TopicAdmin(admin.ModelAdmin):

    list_display = ('name','getSongCount')


class GenreAdmin(admin.ModelAdmin):

    list_display = ('name','getSongCount')


class Song_TopicAdmin(admin.ModelAdmin):
    pass


class Song_GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Topic, TopicAdmin)
admin.site.register(Genre, GenreAdmin)

admin.site.register(Song_Topic, Song_TopicAdmin)
admin.site.register(Song_Genre, Song_GenreAdmin)
