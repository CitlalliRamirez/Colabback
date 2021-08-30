from django.db import models
from alumno.models import Alumno
from profesor.models import Profesor

class Curso(models.Model):
    curso_nombre = models.CharField(max_length=60)
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE,
                                 null=False, blank=False)