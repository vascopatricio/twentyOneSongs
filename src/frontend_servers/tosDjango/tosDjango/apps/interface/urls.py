from django.conf.urls import url

from tosDjango.apps.interface.views import *

urlpatterns = [
    url(r'^exportData/$', exportDataView),

    url(r'^(\w+)/(\w+)/(\w+)/$', interfaceView),
]
