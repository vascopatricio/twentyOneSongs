from django.http import HttpResponseRedirect


def renderInterfacePage(request, javascriptMode, apiMode, argPage):
    """
    """

    from tosDjango.apps.audio.models import Song
    from tosDjango.apps.metadata.models import Genre, Topic
    from django.shortcuts import render_to_response
    from tosDjango.apps.interface.constants import LIBRARY_NAMES, API_MODES, SERVER_RENDERERS, \
        getDictAsList
    from tosDjango.apps.interface.utils.header import obtainHeaderMenu

    variables = {
        'hideSlider': False,
        'page': 'home'
    }

    print("[RenderInterFacePage] Called with ", javascriptMode, apiMode, argPage)

    if javascriptMode not in ['angular', 'react', 'meteor', 'knockout', 'backbone', 'nojs']:
        javascriptMode = 'angular'

    if javascriptMode == 'nojs':
        if argPage in ['browse', 'recomm', 'about']:
            variables['page'] = argPage
            variables['hideSlider'] = True

            if argPage == 'recomm':
                variables['allSongs'] = [s for s in Song.objects.order_by('title')]
                variables['allTopics'] = [t for t in Topic.objects.order_by('name') if len(t.songs.all())]
                variables['allGenres'] = [g for g in Genre.objects.order_by('name') if len(g.songs.all())]

    if apiMode not in ['djangoManual', 'djangoRest', 'node', 'firebase']:
        apiMode = 'djangoManual'

    if 'undefined' in request.get_full_path():
        return HttpResponseRedirect('/interface/'+javascriptMode+'/'+apiMode+'/'+argPage+'/')

    variables['headerMenu'] = obtainHeaderMenu(javascriptMode, apiMode)

    variables['LIBRARY_NAMES'] = getDictAsList(LIBRARY_NAMES, javascriptMode)
    variables['SERVER_RENDERERS'] = getDictAsList(SERVER_RENDERERS, 'django')
    variables['API_MODES'] = getDictAsList(API_MODES, apiMode)

    variables['jsMode'] = javascriptMode
    variables['jsModeToStr'] = LIBRARY_NAMES[javascriptMode] or ''
    variables['apiMode'] = apiMode
    variables['apiModeToStr'] = API_MODES[apiMode] or ''

    return render_to_response('interface.html', variables)
