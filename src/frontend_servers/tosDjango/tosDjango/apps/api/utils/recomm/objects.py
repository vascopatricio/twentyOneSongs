from tosDjango.apps.api.utils.recomm.calc import calculateSongSimilarity, calculateSongTopicSimilarity, \
    calculateSongGenreSimilarity


def obtainRecommendationsForMode(mode, id):
    """
    """

    printPrefix = "[ObtainRecommendations] "

    # print(printPrefix+" Called with mode/id: ",mode,id)

    if mode == 'song':
        return obtainRecommsForSong(id)

    elif mode == 'genre':
        return obtainRecommsForGenre(id)

    elif mode == 'topic':
        return obtainRecommsForTopic(id)

    return []


def obtainRecommsForSong(songId):
    """
    """

    from tosDjango.apps.audio.models import Song

    try:
        song = Song.objects.get(id=songId)
    except:
        # print("Could not get song")
        return []

    scoresBySongId = {}

    for otherSong in Song.objects.exclude(id=songId):
        scoresBySongId[otherSong.id] = calculateSongSimilarity(song, otherSong)

    return obtainSongsResultsArrayFromDictionaryByScore(scoresBySongId)


def obtainRecommsForGenre(genreId):
    """
    """

    from tosDjango.apps.audio.models import Song
    from tosDjango.apps.metadata.models import Genre

    try:
        genre = Genre.objects.get(id=genreId)
    except:
        # print("Could not get song")
        return []

    scoresBySongId = {}

    for eachSong in Song.objects.all():
        res = calculateSongGenreSimilarity(genre, eachSong)
        print("RES:",res)
        scoresBySongId[eachSong.id] = res

    print(scoresBySongId)

    return obtainSongsResultsArrayFromDictionaryByScore(scoresBySongId)


def obtainRecommsForTopic(topicId):
    """
    """

    songs = []

    from tosDjango.apps.audio.models import Song
    from tosDjango.apps.metadata.models import Topic

    try:
        topic = Topic.objects.get(id=topicId)
    except:
        # print("Could not get song")
        return []

    scoresBySongId = {}

    for eachSong in Song.objects.all():
        res = calculateSongTopicSimilarity(topic, eachSong)
        print("RES:", res)
        scoresBySongId[eachSong.id] = res

    return obtainSongsResultsArrayFromDictionaryByScore(scoresBySongId)


def obtainSongsResultsArrayFromDictionaryByScore(scoresBySongId):
    """
    """

    from tosDjango.apps.audio.models import Song

    songs = []

    for key, value in scoresBySongId.items():
        song = Song.objects.get(id=key)
        songs.append([song, value[0], value[1]])

    songs.sort(key=lambda x: x[1], reverse=True)

    return songs