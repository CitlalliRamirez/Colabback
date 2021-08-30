from django.db.models import fields
from .models import Administrador
from rest_framework import serializers

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'