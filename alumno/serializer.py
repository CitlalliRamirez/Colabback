from django.db.models import fields
from .models import Alumno
from rest_framework import serializers

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'