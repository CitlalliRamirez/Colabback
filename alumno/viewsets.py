from rest_framework import serializers, viewsets
from .models import Alumno
from .serializer import AlumnoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer