from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from profiles import urls as profile_urls
from chat import urls as chat_urls
from home import urls as home_urls
from account import urls as account_urls
from checkout import urls as subscribe_urls
from search import urls as search_urls
from django.views.static import serve
from .settings import MEDIA_ROOT



urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    path('', include(home_urls)),
    path('accounts/', include(profile_urls)),
    path('chat/', include(chat_urls)),
    path('subscribe/', include(subscribe_urls)),
    path('my-account/', include(account_urls)),
    path('search/', include(search_urls)),
    #path('media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}) 
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

