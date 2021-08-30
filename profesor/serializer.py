from django.db.models import fields
from .models import Profesor
from rest_framework import serializers

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'