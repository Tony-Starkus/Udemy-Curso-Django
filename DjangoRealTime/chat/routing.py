from django.urls import re_path  # Criar path com expressões regulares
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', ChatConsumer)
]
