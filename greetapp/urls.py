from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url

urlpatterns = [
    path('', home, name='home'),
    path('send', multimail1, name="mailsend"),
    path('thanks', greet, name="greet"),
    
    # url(r'^image_load/$', image_load, name='image_load'),
    path('image_load/', image_load, name='image_load'),

    # path('send/render_image/',render_image, name='render_image'),
    # path('send/', SendTemplateMailView.as_view(), name=    'send_template'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
