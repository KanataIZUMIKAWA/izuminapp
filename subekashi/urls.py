from django.contrib import admin
from django.urls import path, include
from subekashi.views import *
from rest_framework import routers

app_name='subekashi'

defaultRouter = routers.DefaultRouter()
defaultRouter.register('song', SongAPI)
defaultRouter.register('ai', AiAPI)
defaultRouter.register('ad', AdAPI)

urlpatterns = [
    path('admin', admin.site.urls),
    path('', top, name='top'),
    path('new', new, name='new'),
    path('delete', delete, name='delete'),
    path('songs', search, name='search'),
    path('songs/<int:songId>', song, name='song'),
    path('channel/<str:channelName>', channel, name='channel'),
    path('search', search, name='search_sub'),  #いつか消す
    path('ai', ai, name='ai'),
    path('setting', setting, name='setting'),
    path('ad', ad, name='ad'),
    path('ad/complete', ad_complete, name='ad_complete'),
    path('research', research, name='research'),
    path('special', special, name='special'),
    path('robots.txt', robots, name='robots'),
    path('sitemap.xml', sitemap, name='sitemap'),
    path('favicon.ico', favicon, name='favicon'),
    path('.well-known/traffic-advice', trafficAdvice, name='traffic-advice'),
    path('api/',include(defaultRouter.urls)),
    path('api/html/song_cards', song_cards, name='song_cards'),
    path('api/html/song_guessers', song_guessers, name='song_guessers'),
]