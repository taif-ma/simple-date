from django.conf.urls import url
from .views import index, preregister, channel_js

urlpatterns = [
    url(r'^$', preregister, name='preregister'),
    url(r'^home/', index, name="index"),
    url(r'^channel.js$', channel_js),
]
