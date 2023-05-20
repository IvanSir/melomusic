from channels.generic.websocket import AsyncWebsocketConsumer
import json

from shared_rooms.models import ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the room_id from the URL
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_id

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope["user"]

        # Save the chat message
        ChatMessage.objects.create(
            message=message,
            room_id=self.room_id,
            user=user
        )

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': user.username
            }
        )

    async def chat_message(self, event):
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username']
        }))
