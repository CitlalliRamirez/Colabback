from django.db.models import fields
from .models import Alumnocurso
from rest_framework import serializers

class AlumnocursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnocurso
        fields = '__all__'