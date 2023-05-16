from django.contrib import admin

from shared_rooms.models import ChatMessage, SharedRoom

# Register your models here.
admin.site.register(SharedRoom)
admin.site.register(ChatMessage)