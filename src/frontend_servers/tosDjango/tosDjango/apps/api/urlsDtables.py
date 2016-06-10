from django.conf.urls import url

from tosDjango.apps.api.views.apiDtables import *

urlpatterns = [
    url(r'^albums/$', albumsDtableRes),
    url(r'^songs/$', songsDtableRes),

    url(r'^recommendations/(\w+)/(\d+)/$', recommendationsDtableRes)
]