from django.urls import path
from chatserver import consumers

websocket_urlpatterns = [
  path('chatroom/<str:user>', consumers.ChatConsumer),
]