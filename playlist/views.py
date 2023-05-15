from django.shortcuts import render, redirect
from django.contrib import messages
from genre.models import Genre
from music.models import Music
from core.tasks import send_email_task
from playlist.models import Playlist

def PlaylistsPage(request):
    '''Releases albums view page'''
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    get_genres = Genre.objects.all()
    context = {'albums' : 'albumbs', 'genres' : get_genres, 'player' : new_song_for_player}
    
    return render(request, 'playlist/playlists.html', context)


def SinglePlaylistPage(request, pk):
    '''Signle album page view'''
    playlist = Playlist.objects.get(id=pk)

    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    songs = playlist.music.all()
    songs_count = songs.count()
    
    context = {
        'playlist' : playlist, 
        'songs' : songs, 
        'count' : songs_count,
        'player' : new_song_for_player, 
    }
    
    return render(request, 'playlist/single-playlist.html', context)