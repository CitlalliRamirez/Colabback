from django.db.models import fields
from .models import Alumnochat
from rest_framework import serializers

class AlumnochatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnochat
        fields = '__all__'