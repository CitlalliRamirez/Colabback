from rest_framework import serializers, viewsets
from .models import Alumnochat
from .serializer import AlumnochatSerializer

class AlumnochatViewSet(viewsets.ModelViewSet):
    queryset = Alumnochat.objects.all()
    serializer_class = AlumnochatSerializer