
def getAlbumThumbUrlByAlbum(album):
    """
    """

    thumbsByAlbum = {
        'blurryface': 'http://static.vascopatricio.com/twentyonesongs/album/blurryface.jpg'
    }

    key = 'blurryface'

    try:
        return album.thumbUrl
    except:
        return ''