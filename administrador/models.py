from django.db import models
from usuario.models import Usuario
# Create your models here.
class Administrador(models.Model):
    administrador_nombre = models.CharField(max_length=60)
    usuario = models.OneToOneField(Usuario,
                                on_delete=models.CASCADE,
                                null=False,blank=False)