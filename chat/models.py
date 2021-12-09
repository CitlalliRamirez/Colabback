from django.db import models
from profesor.models import Profesor
from curso.models import Curso

class Chat(models.Model):
    chat_nombre = models.CharField(max_length=60)
    chat_conversacion = models.CharField(max_length=40000)
    chat_fecha= models.CharField(max_length=255)
    chat_hora=models.TimeField()
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE,
                                 null=False, blank=False)     
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE,
                                 null=False, blank=False)                        