from django.shortcuts import render, redirect
from django.contrib import messages
from music.models import Music, MusicComment
from album.models import Album
from music.forms import MusicCommentForm
from music.utils import Search
from core.tasks import send_email_task 
from playlist.models import Playlist, PlaylistToMusic

def SongsPage(request):
    '''Songs page view'''
    songs = Search(request)
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    context = {'songs' : songs, 'player' : new_song_for_player}

    return render(request, 'music/songs.html', context)


def SingleSongPage(request, slug, pk):
    '''Single song page view'''
    song = Music.objects.get(slug=slug, pk=pk)
    form = MusicCommentForm()

    if request.method == 'POST':
        form = MusicCommentForm(request.POST)
        if form.is_valid():
            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            
            if reply_id:
                reply_obj = MusicComment.objects.get(id=reply_id)

            if reply_obj:
                comment = form.save(commit=False)
                comment.music = song
                comment.owner = request.user
                comment.reply = reply_obj
                comment.save()
            
            else:
                comment = form.save(commit=False)
                comment.music = song
                comment.owner = request.user
                comment.save()

            messages.success(request, 'Successfully Submitted. Your comment will be available after review.')
            # Send email to user using celery
            send_email_task.delay(comment.owner.email)
            return redirect('single-song', slug=song.slug, pk=song.id)

    # Songs from this artist
    artist_albums = Album.objects.filter(artists=song.artists.first())[:6]
    music_comments_count = song.musiccomment_set.filter(active=True).count()
    
    fav_playlist = request.user.playlists.get(title='Favourites')
    
    is_favourite = song in fav_playlist.music.all()
    context = {
        'song' : song, 
        'player' : song,
        'artist_albums' : artist_albums,
        'form' : form,
        'comments_count' : music_comments_count,
        'is_favourite': is_favourite
    }

    return render(request, 'music/single-song.html', context)



def add_favourite(request, slug, pk):
    '''Songs page view'''
    song = Music.objects.get(slug=slug, pk=pk)
    
    fav_playlist = request.user.playlists.get(title='Favourites')
    fav_playlist.music.add(song)
    

    return redirect('single-song', slug,pk)


def remove_favourite(request, slug, pk):
    '''Songs page view'''
    song = Music.objects.get(slug=slug, pk=pk)
    
    fav_playlist = request.user.playlists.get(title='Favourites')
    fav_playlist.music.remove(song)
    

    return redirect('single-song', slug,pk)


def get_news(request):
    friends = request.user.friends.all()
    favourites = Playlist.objects.filter(owner__in=friends)
    
    playlist_to_music = PlaylistToMusic.objects.filter(playlist__in=favourites).order_by('added_at')

    
    
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    context = {
        'playlist_to_music' : playlist_to_music, 
        'player' : new_song_for_player
    }

    
    return render(request, 'music/news.html', context)
