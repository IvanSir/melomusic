from django.db import models
from core.models import User


class SharedRoom(models.Model):
    name = models.CharField(max_length=255)
    is_private = models.BooleanField(default=False)
    songs = models.ManyToManyField(to="music.Music", related_name="song_rooms")
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_rooms"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=8, null=True, blank=True)
    max_members = models.IntegerField(null=True, blank=True)
    participants = models.ManyToManyField(to='core.User')


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        SharedRoom, on_delete=models.CASCADE, related_name="chat_messages"
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
