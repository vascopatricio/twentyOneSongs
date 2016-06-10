def calculateSongSimilarity(songA, songB):
    """
    """

    simil = 0.0
    justifs = []

    genreScore = 0.0
    topicScore = 0.0
    albumSore = 0.0
    paceScore = 0.0

    genresA = [gRel.genre for gRel in songA.genres.all()]
    genresB = [gRel.genre for gRel in songB.genres.all()]
    topicsA = [tRel.topic for tRel in songA.topics.all()]
    topicsB = [tRel.topic for tRel in songB.topics.all()]

    # print("Genres A/B:",genresA,genresB)
    # print("Topics A/B:",topicsA,topicsB)

    if songA.getAlbum() == songB.getAlbum():
        albumSore = 1.0
        justifs.append('Same album')

    if songA.pace == songB.pace:
        albumSore = 2.0
        justifs.append('Same pace ('+str(songA.pace)+')')

    for genre in genresA:
        if genre in genresB:
            genreScore += 5.0
            justifs.append('Genre: ' + str(genre) + '')

    for topic in topicsA:
        if topic in topicsB:
            topicScore += 5.0
            justifs.append('Topic: ' + str(topic) + '')

    simil = genreScore + topicScore + albumSore + paceScore

    return simil, justifs


def calculateSongTopicSimilarity(topic, song):
    """
    """

    topicIds = [str(rel.topic.id) for rel in song.topics.all()]

    score = 0.0
    justifs = []

    if str(topic.id) in topicIds:
        score += 5.0
        justifs.append('Topic: ' + str(topic) + '')

    return score, justifs


def calculateSongGenreSimilarity(genre, song):
    """
    """

    genreIds = [str(rel.genre) for rel in song.genres.all()]

    score = 0.0
    justifs = []

    if str(genre) in genreIds:
        score += 5.0
        justifs.append('Topic: ' + str(genre) + '')

    return score, justifs
