from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from music.models import Music
from shared_rooms.models import ChatMessage, SharedRoom
from shared_rooms.consumers import ChatConsumer
from asgiref.sync import async_to_sync


def SharedRoomsPage(request):
    shared_rooms = SharedRoom.objects.all()
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    context = {'shared_rooms': shared_rooms, 'player': new_song_for_player}
    return render(request, 'shared_rooms/rooms.html', context)


def SingleRoomPage(request, pk):
    shared_room = SharedRoom.objects.get(id=pk)
    shared_room.participants.add(request.user)
    chat_messages = ChatMessage.objects.filter(room=shared_room)
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    context = {'room': shared_room, 'chat_messages': chat_messages, 'player': new_song_for_player}
    return render(request, 'shared_rooms/single-room.html', context)


def SendChatMessage(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(SharedRoom, id=room_id)
        sender = request.user
        content = request.POST['message']
        ChatMessage.objects.create(
            message=content,
            room=room,
            user=sender
        )
# Send the message to the room group
        ChatConsumer.send_chat_message_to_group(room_id, content, sender.username)

        # Redirect back to the shared music room
        return redirect('single-room', room_id)


@staticmethod
def send_chat_message_to_group(room_id, message, username):
    from channels.layers import get_channel_layer
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'chat_{room_id}',
        {
            'type': 'chat_message',
            'message': message,
            'username': username
        }
    )
