from django.contrib import admin
from . import views
from django.urls import path,include
from rest_framework import routers

app_name = 'subeana'

defaultRouter = routers.DefaultRouter()
defaultRouter.register('song', views.SongViewSet)
defaultRouter.register('ai', views.AiViewSet)

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.top, name = 'top'),
    path('new', views.new, name = 'new'),
    path('make', views.make, name = 'make'),
    path('edit', views.edit, name = 'edit'),
    path('songs/<int:song_id>', views.song, name = 'song'),
    path('channel/<str:channel_name>', views.channel, name = 'channel'),
    path('api/',include(defaultRouter.urls)),
    path('error', views.error, name = 'error'),
    path('dev', views.dev, name = 'dev'),
]