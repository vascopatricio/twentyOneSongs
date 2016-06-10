
def obtainHeaderMenu(js, api):
    """
    Function to return the header bar based on the chosen JavaScript library and API engine.
    """

    homeEntry = {'name': 'Home'}
    browserEntry = {'name': 'Browser'}
    recommEntry = {'name': 'Recommender'}
    aboutEntry = {'name': 'About'}

    if js == 'angular':
        homeEntry['href'] = '#agHome'
        browserEntry['href'] = '#agBrowse'
        recommEntry['href'] = '#agRecomm'
        aboutEntry['href'] = '#agAbout'
    elif js == 'react':
        pass
    elif js == 'nojs':
        homeEntry['href'] = '/interface/'+ js+'/' + api + '/home/'
        browserEntry['href'] = '/interface/' + js+'/' + api + '/browse/'
        recommEntry['href'] = '/interface/' + js+'/' + api + '/recomm/'
        aboutEntry['href'] = '/interface/' + js+'/' + api + '/about/'

    menu = [
        homeEntry,
        browserEntry,
        recommEntry,
        aboutEntry
    ]

    return menu
