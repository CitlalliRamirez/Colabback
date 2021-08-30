from rest_framework import serializers, viewsets
from .models import Curso
from .serializer import CursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer