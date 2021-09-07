from django.db import models
from profesor.models import Profesor
from curso.models import Curso

class Chat(models.Model):
    chat_nombre = models.CharField(max_length=60)
    chat_conversacion = models.CharField(max_length=60)
    chat_fecha_hora= models.DateTimeField(auto_now_add=True)
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE,
                                 null=False, blank=False)     
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE,
                                 null=False, blank=False)                        