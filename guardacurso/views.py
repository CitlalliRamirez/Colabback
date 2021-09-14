from django.shortcuts import render
from django.http import HttpResponse
from curso.models import Curso
from alumno.models import Alumno
from alumnocurso.models import Alumnocurso
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def guarda(request):
    data = ''
    numAlumnos=0
    d=0
    if request.method=='POST':
        nombre = request.POST.get('nombre')
        semestre = request.POST.get('semestre')
        carrera = request.POST.get('carrera')
        idprofesor = request.POST.get('idprofesor')
        numAlumnos = Alumno.objects.filter(alumno_semestre=semestre,alumno_carrera=carrera).count()
        listaAlumn = Alumno.objects.filter(alumno_semestre=semestre,alumno_carrera=carrera)
        if numAlumnos>=4:
            data='ok'
            Curso.objects.create(curso_nombre=nombre,profesor_id=idprofesor)
            idcurso = Curso.objects.last().id
            for i in range(numAlumnos):
                Alumnocurso.objects.create(curso_id=idcurso,alumno_id=listaAlumn[i].pk)
        else:
            data='no'
            
    return HttpResponse(data)
