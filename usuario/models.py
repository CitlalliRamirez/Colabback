from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario_correo = models.CharField(max_length=40)
    usuario_contrasena = models.CharField(max_length=20)

