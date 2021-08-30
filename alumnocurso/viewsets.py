from rest_framework import serializers, viewsets
from .models import Alumnocurso
from .serializer import AlumnocursoSerializer

class AlumnocursoViewSet(viewsets.ModelViewSet):
    queryset = Alumnocurso.objects.all()
    serializer_class = AlumnocursoSerializer