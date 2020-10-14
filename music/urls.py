from django.conf.urls import url
from . import views
from .views import album_favorite

app_name = 'music'
urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    url(r'^register/$', views.UserFormView.as_view(), name = 'register'),
    #/music/123
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    # /music/123/favorite/
    url(r'album/add/$', views.AlbumCreate.as_view(), name = 'album-add'),

    url(r'^(?P<album_id>[0-9]+)/album_favorite/$', views.album_favorite, name = 'album-favorite'),

    #/music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(),name = 'album-update'),
    #/music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name = 'album-delete'),

]