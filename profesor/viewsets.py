from rest_framework import serializers, viewsets
from .models import Profesor
from .serializer import ProfesorSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer