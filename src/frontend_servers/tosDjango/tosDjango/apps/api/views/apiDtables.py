def albumsDtableRes(request):
    """
    """

    from tosDjango.apps.audio.models import Album
    from tosDjango.apps.api.utils.serialization import obtainAlbumJQueryDtableRow, returnJQueryDatatableJsonResponse

    aaData = []

    albums = Album.objects.all()
    for album in albums:
        aaData.append(obtainAlbumJQueryDtableRow(album))

    return returnJQueryDatatableJsonResponse(aaData)


def songsDtableRes(request):
    """
    """

    from tosDjango.apps.audio.models import Song_Album
    from tosDjango.apps.api.utils.serialization import obtainSongJQueryDtableRow, returnJQueryDatatableJsonResponse

    aaData = []

    songRels = Song_Album.objects.all()
    for rel in songRels:
        aaData.append(obtainSongJQueryDtableRow(rel.song, 'standard'))

    return returnJQueryDatatableJsonResponse(aaData)


def recommendationsDtableRes(request, mode, id):
    """
    """

    from tosDjango.apps.audio.models import Song_Album
    from tosDjango.apps.api.utils.recomm.objects import obtainRecommendationsForMode
    from tosDjango.apps.api.utils.serialization import obtainSongJQueryDtableRow, returnJQueryDatatableJsonResponse

    aaData = []

    songTuples = obtainRecommendationsForMode(mode, id)
    for songTuple in songTuples:
        extraParams = {'score': songTuple[1], 'justifs': songTuple[2]}
        aaData.append(obtainSongJQueryDtableRow(songTuple[0], 'recommRes', extraParams=extraParams))

    return returnJQueryDatatableJsonResponse(aaData)