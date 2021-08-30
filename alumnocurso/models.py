from django.db import models
from alumno.models import Alumno
from curso.models import Curso

class Alumnocurso(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE,
                                 null=False, blank=False)
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE,
                                 null=False, blank=False)