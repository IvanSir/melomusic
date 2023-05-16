from django.urls import path
from playlist import views

urlpatterns = [
    path('playlists/', views.PlaylistsPage, name='playlists'),
    path('playlists/<pk>/', views.SinglePlaylistPage, name='single-playlist'),
    path('playlists/<pk>/copy/', views.copy_playlist, name='copy-playlist'),
    path('playlists/<pk>/uncopy/', views.uncopy_playlist, name='uncopy-playlist'),
]