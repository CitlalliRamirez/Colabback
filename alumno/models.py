from django.db import models
from usuario.models import Usuario
# Create your models here.
class Alumno(models.Model):
    alumno_nombre = models.CharField(max_length=60)
    alumno_semestre = models.CharField(max_length=20)
    alumno_carrera = models.CharField(max_length=40)
    usuario = models.OneToOneField(Usuario,
                                on_delete=models.CASCADE,
                                null=False,blank=False)