from django.http import HttpResponse
from usuario.models import Usuario
from profesor.models import Profesor
from administrador.models import Administrador
from alumno.models import Alumno
from django.core import serializers
import json

class lista_usuarios():
    def __init__(self,nombre,correo,id,contrasena,tipo,idtipo):
        self.nombre = nombre
        self.correo = correo
        self.id = id
        self.contrasena = contrasena
        self.tipo = tipo
        self.idtipo = idtipo
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# Create your views here.
def jsonDefault(object):
    return object.__dict__

    
def listado(request):
    cad = []
    nombreProfe = Profesor.objects.all()
    nombreAlum = Alumno.objects.all() 
    nombreAdm = Administrador.objects.all()  
    for profe in nombreProfe:
        obj = lista_usuarios(profe.profesor_nombre, profe.usuario.usuario_correo,profe.usuario.id,profe.usuario.usuario_contrasena,"Profesor",profe.id)
        cad.append(json.loads(obj.toJSON()))
     
    for alum in nombreAlum:
        obj = lista_usuarios(alum.alumno_nombre, alum.usuario.usuario_correo,alum.usuario.id,alum.usuario.usuario_contrasena,"Alumno",alum.id)
        cad.append(json.loads(obj.toJSON()))

    for adm in nombreAdm:
        obj = lista_usuarios(adm.administrador_nombre, adm.usuario.usuario_correo,adm.usuario.id,adm.usuario.usuario_contrasena,"Administrador",adm.id)
        cad.append(json.loads(obj.toJSON()))

    return HttpResponse(json.dumps(cad))    
