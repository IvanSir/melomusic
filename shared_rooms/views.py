from django.shortcuts import render

from music.models import Music
from shared_rooms.models import SharedRoom

# Create your views here.
def SharedRoomsPage(request):
    '''Songs page view'''
    shared_rooms = SharedRoom.objects.all()
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    context = {'shared_rooms' : shared_rooms, 'player' : new_song_for_player}

    return render(request, 'shared_rooms/rooms.html', context)

def SingleRoomPage(request, pk):
    '''Songs page view'''
    shared_room = SharedRoom.objects.get(id=pk)
    shared_room.participants.add(request.user)
    
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    context = {'shared_room' : shared_room, 'player' : new_song_for_player}

    return render(request, 'shared_rooms/single-room.html', context)