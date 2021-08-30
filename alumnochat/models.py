from django.db import models
from alumno.models import Alumno
from chat.models import Chat

class Alumnochat(models.Model):
    rol = models.CharField(max_length=20)
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE,
                                 null=False, blank=False)
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE,
                                 null=False, blank=False)