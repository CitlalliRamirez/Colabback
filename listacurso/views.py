from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from alumnocurso.models import Alumnocurso
from profesor.models import Profesor
from curso.models import Curso
from alumno.models import Alumno
from django.core import serializers
import json

class lista_cursos():
    def __init__(self,nombre,semestre,id,carrera,idprofesor):
        self.nombre = nombre
        self.semestre = semestre
        self.id = id
        self.carrera = carrera
        self.idprofesor = idprofesor
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# Create your views here.
def jsonDefault(object):
    return object.__dict__

    
def listadocurso(request):
    cad = []
    cursos = Curso.objects.all()
    data=''
    for curso in cursos:
        alumnoc = Alumnocurso.objects.filter(curso=curso.id).last()
        alumnoId = alumnoc.alumno.id
        datosAlum = Alumno.objects.filter(id=alumnoId)
        data = datosAlum[0].alumno_carrera
        obj = lista_cursos(curso.curso_nombre, datosAlum[0].alumno_semestre,curso.id,datosAlum[0].alumno_carrera,curso.profesor.id)
        cad.append(json.loads(obj.toJSON()))

    return HttpResponse(json.dumps(cad))    
