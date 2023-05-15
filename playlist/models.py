from django.db import models
from django.contrib.auth import get_user_model

class Playlist(models.Model):
    '''Playlist model'''
    title = models.CharField(max_length=220, default='Favourites')
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='playlists')
    is_private = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='PlaylistPictures/', default='PlaylistPictures/default.jpg')
    music = models.ManyToManyField(to='music.Music')

    def __str__(self):
        return self.title

