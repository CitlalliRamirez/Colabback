from rest_framework import serializers, viewsets
from .models import Administrador
from .serializer import AdministradorSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer