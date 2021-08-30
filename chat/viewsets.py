from rest_framework import serializers, viewsets
from .models import Chat
from .serializer import ChatSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer