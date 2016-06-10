LIBRARY_NAMES = {
    'nojs': 'No JavaScript',
    'angular': 'AngularJS',
    'react': 'React.js',
    'knockout': 'Knockout.js',
    'meteor': 'Meteor.js',
    'backbone': 'Backbone.js'
}

SERVER_RENDERERS = {
    'django': 'Django',
    'flask': 'Flask',
    'node': 'Node.js',
}

API_MODES = {
    'node': 'Node.js',
    'djangoManual': 'Django Manual API',
    'djangoRest': 'Django REST Framework',
    'firebase': 'Firebase',
}

API_SERVER_LOCATIONS = {
    "node": "http://localhost:8000/api/",
    "djangoManual": "http://localhost:8000/api/",
    "djangoRest": "http://localhost:8000/api/",
    "firebase": "http://localhost:8000/api/",
}

def getDictAsList(dict, selectIfEqualTo):
    """
    """

    vals = []

    for key, value in dict.iteritems():
        obj = {'key': key, 'value': value}
        if selectIfEqualTo == key:
            obj['selected'] = True
        vals.append(obj)

    return vals
