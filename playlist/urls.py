from django.urls import path
from playlist import views

urlpatterns = [
    path('playlists/', views.PlaylistsPage, name='playlists'),
    path('playlists/<pk>/', views.SinglePlaylistPage, name='single-playlist')
]