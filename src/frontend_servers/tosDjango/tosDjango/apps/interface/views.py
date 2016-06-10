from django.http import HttpResponse


def exportDataView(request):
    """
    """

    import os
    import datetime

    exportFolder = os.path.dirname(__file__)+'/../../dataExport/'

    today = str(datetime.date.today())
    print(today)

    try:
        os.mkdir(exportFolder+'/'+today)
    except:
        pass

    exportDataForDayAndFolder(exportFolder+'/'+today+'/')

    return HttpResponse('Exported OK')

def exportDataForDayAndFolder(exportFolder):
    """
    """

    from django.http import HttpResponseRedirect
    from tosDjango.apps.audio.models import Song, Album, Song_Album
    from tosDjango.apps.metadata.models import Topic, Genre, Song_Topic, Song_Genre

    print(exportFolder)

    songsJson = []
    for song in Song.objects.all():
        songsJson.append(song.toJSON())
    writeJsonToFile(songsJson, exportFolder + 'songs.json')

    albJson = []
    for alb in Album.objects.all():
        albJson.append(alb.toJSON())
    writeJsonToFile(albJson, exportFolder + 'albums.json')

    relsJson = []
    for rel in Song_Album.objects.all():
        relsJson.append(rel.toJSON())
    writeJsonToFile(relsJson, exportFolder + 'songAlbumRels.json')

    genresJson = []
    for genre in Genre.objects.all():
        genresJson.append(genre.toJSON())
    writeJsonToFile(genresJson, exportFolder + 'genres.json')

    topicsJson = []
    for topic in Topic.objects.all():
        topicsJson.append(topic.toJSON())
    writeJsonToFile(topicsJson, exportFolder + 'topics.json')

    relsJson = []
    for rel in Song_Genre.objects.all():
        relsJson.append(rel.toJSON())
    writeJsonToFile(relsJson, exportFolder + 'songGenreRels.json')

    relsJson = []
    for rel in Song_Topic.objects.all():
        relsJson.append(rel.toJSON())
    writeJsonToFile(relsJson, exportFolder + 'songTopicRels.json')

    return

def writeJsonToFile(contents, fName):
    """
    """

    import json

    with open(fName, 'w') as outfile:
        json.dump(contents, outfile)

    return

def mainRedirect(request):
    """
    """

    from django.http import HttpResponseRedirect

    return HttpResponseRedirect('/interface/nojs/djangoManual/home/')


def interfaceView(request, javascriptMode, apiMode, page):
    """
    View for the Twenty One Songs interface.
    Choose the JavaScript library and the API Mode and it will render.

    """

    from tosDjango.apps.interface.utils.rendering import renderInterfacePage

    return renderInterfacePage(request, javascriptMode, apiMode, page)

