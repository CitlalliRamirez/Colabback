from django.db import models
from usuario.models import Usuario
# Create your models here.
#para acceder a la relacion -> la clase relacionada en minusc_set
#filtros, count, agrup
class Profesor(models.Model):
    profesor_nombre = models.CharField(max_length=60)
    usuario = models.OneToOneField(Usuario,
                                on_delete=models.CASCADE,
                                null=False,blank=False)
