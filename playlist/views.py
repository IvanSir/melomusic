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
    playlists = Playlist.objects.filter(owner=request.user)
    copied_playlists = Playlist.objects.filter(copies=request.user)
    
    context = {'playlists' : playlists, 'copied_playlists': copied_playlists, 'genres' : get_genres, 'player' : new_song_for_player}
    
    return render(request, 'playlist/playlists.html', context)


def SinglePlaylistPage(request, pk):
    '''Signle album page view'''
    playlist = Playlist.objects.get(id=pk)

    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    songs = playlist.music.all()
    songs_count = songs.count()
    
    is_copied = playlist in request.user.copy_playlists.all()
    
    is_not_owner = playlist not in request.user.playlists.all()
    
    context = {
        'playlist' : playlist, 
        'songs' : songs, 
        'count' : songs_count,
        'player' : new_song_for_player, 
        'is_copied': is_copied,
        'is_not_owner': is_not_owner
    }
    
    return render(request, 'playlist/single-playlist.html', context)


def copy_playlist(request, pk):
    '''Signle album page view'''
    playlist = Playlist.objects.get(id=pk)
    if playlist in request.user.copy_playlists.all():
        messages.error(request, "Copied playlist already exists.")
    else:
        request.user.copy_playlists.add(playlist)
        messages.success(request, "Playlist successfully copied.")
    
    return redirect('single-playlist', pk)


def uncopy_playlist(request, pk):
    '''Signle album page view'''
    playlist = Playlist.objects.get(id=pk)
    if playlist not in request.user.copy_playlists.all():
        messages.error(request, "No Copied playlist already exists.")
    else:
        request.user.copy_playlists.remove(playlist)
        messages.success(request, "Copied playlist was successfully removed.")
    
    return redirect('single-playlist', pk)