from django.contrib import admin

from playlist.models import Playlist

class PlaylistAdmin(admin.ModelAdmin):
    '''Album admin page'''
    list_display = ['title', 'id']
    search_fields = ['title']




admin.site.register(Playlist, PlaylistAdmin)