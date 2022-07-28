from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url

urlpatterns = [
    path('', home, name='home'),
    path('send', multimail2, name="mailsend"),
    path('thanks', greet, name="greet"),
    
    # url(r'^image_load/$', image_load, name='image_load'),
    url(r'^Opened/\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+$/', Opened, name='Opened'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#_(\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})

# r'^users/\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+$/'

# (?P<data>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$