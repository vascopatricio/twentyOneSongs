def obtainAlbumJQueryDtableRow(album):
    """
    Function to obtain a jQuery datatable row for a given album.
    """

    return [
        obtainAlbumJQueryDtableCell(album, 'title'),
        obtainAlbumJQueryDtableCell(album, 'year'),
    ]


def obtainSongJQueryDtableRow(song, rowFormat, extraParams={}):
    """
    Function to obtain a jQuery datatable row for a given song.
    """

    if rowFormat not in ['standard', 'recommRes']:
        rowFormat = 'standard'

    row = [
        obtainSongJQueryDtableCell(song, 'albThumbTitle'),
        obtainSongJQueryDtableCell(song, 'duration'),
        obtainSongJQueryDtableCell(song, 'genres'),
        obtainSongJQueryDtableCell(song, 'topics'),
    ]

    if rowFormat == 'recommRes':
        row = [
            obtainSongJQueryDtableCell(song, 'albThumbTitle'),
            obtainSongJQueryDtableCell(song, 'duration'),
            obtainSongJQueryDtableCell(song, 'match', extraParams=extraParams),
            obtainSongJQueryDtableCell(song, 'listen')
        ]

    return row


def obtainAlbumJQueryDtableCell(album, colName):
    """
    """

    html = ''

    if colName == 'title':
        html += str(album.title)

    elif colName == 'year':
        html += str(album.year)

    return html


def obtainSongJQueryDtableCell(song, colName, extraParams=None):
    """
    """

    from tosDjango.apps.audio.constants import getAlbumThumbUrlByAlbum

    extraParams = extraParams or {}

    html = ''

    if colName == 'title':
        html += str(song.title)

    elif colName == 'albThumbTitle':
        html += '<div class="row">'
        html += '<div class="col-md-4">'
        thumb = getAlbumThumbUrlByAlbum(song.getAlbum())
        if len(thumb):
            html += '<img src="'+thumb+'" style="max-height: 75px; min-height: 35px; min-width: 35px; width: auto;">'
            html += '</img>'
        html += '</div>'
        html += '<div class="col-md-8">'
        html += obtainSongJQueryDtableCell(song, 'title')
        html += '</div>'
        html += '</div>'

    elif colName == 'duration':
        html += str(song.durationToStr())

    elif colName == 'genres':
        genres = song.genres.all()
        if len(genres):
            pass
        else:
            pass

    elif colName == 'topics':
        topics = song.topics.all()
        if len(topics):
            pass
        else:
            pass

    elif colName == 'match':

        score = (extraParams or {})['score'] or 0
        justifs = (extraParams or {})['justifs'] or []

        html += '<span style="display:none;">%04d</span> ' % (score)

        if score > 0:
            justifsDivId = 'songJustifsDiv'+str(song.id)

            html += '<p onclick="$(\'#'+justifsDivId+'\').toggle();">' \
                                                     '<span class="btn btn-xs btn-primary">'+str(score)+'</span></p>'

            html += '<div id="'+justifsDivId+'" style="display:none; min-width: 150px;">'
            html += '<p>'
            for justif in justifs:
                html += '<small>'+justif+'</small><br/>'
            html += '</p>'
            html += '</div>'
        else:
            html += 'N/A'

    elif colName == 'listen':
        ytVideoId = (song.ytVideoLink or '').replace('https://www.youtube.com/watch?v=','')
        ytAudioId = (song.ytAudioLink or '').replace('https://www.youtube.com/watch?v=', '')

        if len(song.ytVideoLink or '') > 0:
            html += ' <a href="'+str(song.ytVideoLink)+'">' \
               '<span class="btn btn-xs btn-primary">YT Vid (Open)</span></a>'
            html += ' <a onclick="embedYoutubeVideo(\'' + str(ytVideoId) +'\');" ' \
              '<span class="btn btn-xs btn-primary">YT Vid (Embed)</span></a>'

        if len(song.ytAudioLink or '') > 0:
            html += ' <a href="' + str(song.ytAudioLink) + '">' \
                       '<span class="btn btn-xs btn-primary">YT Aud (Open)</span></a>'
            html += ' <a onclick="embedYoutubeVideo(\'' + str(ytAudioId) + '\');" ' \
                      '<span class="btn btn-xs btn-primary">YT Aud (Embed)</span></a>'

        if len(song.spotifyLink or '') > 0:
            html += ' <a href="' + str(song.spotifyLink) + '">' \
                                                           '<span class="btn btn-xs btn-primary">Spotify</span></a>'

    return html


def returnJQueryDatatableJsonResponse(aaData):
    """
    """

    from django.http import JsonResponse

    dataDict = {
        'aaData': aaData,
        'iTotalRecords': len(aaData)
    }

    return JsonResponse(dataDict, safe=False)
