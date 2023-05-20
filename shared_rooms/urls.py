from django.urls import path
from shared_rooms import views

urlpatterns = [
    path('shared_rooms/', views.SharedRoomsPage, name='shared_rooms'),
    path('shared_rooms/<pk>/', views.SingleRoomPage, name='single-room'),
    path('shared_rooms/<pk>/send_message/', views.SendChatMessage, name='send-chat-message'),
    path('ws/chat/<room_id>/', views.ChatConsumer.as_asgi()),
]