from rest_framework import serializers, viewsets
from .models import Usuario
from .serializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer