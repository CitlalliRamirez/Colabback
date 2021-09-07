from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from alumnocurso.models import Alumnocurso
from profesor.models import Profesor
from curso.models import Curso
from chat.models import Chat
from alumno.models import Alumno
from alumnochat.models import Alumnochat
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

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

#listar los chats
class lista_chat():
    def __init__(self,nombre,id,fecha,editor,moderador,observador):
        self.nombre = nombre
        self.id = id
        self.fecha = fecha
        self.editor=editor
        self.moderador=moderador
        self.observador=observador
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# Create your views here.
def jsonDefault(object):
    return object.__dict__

@csrf_exempt    
def listadochat(request):
    cad = []
    if request.method=='POST':
        idcurso = request.POST.get('id')
        chats=Chat.objects.filter(curso_id=idcurso)
        for chat in chats:
            cad_obs=[]
            alumn_chat_editor = Alumnochat.objects.filter(chat_id=chat.id,rol='Editor')[0]
            alumn_chat_mod = Alumnochat.objects.filter(chat_id=chat.id,rol='Moderador')[0]
            alumn_chat_obs = Alumnochat.objects.filter(chat_id=chat.id,rol='Observador')
            for i in alumn_chat_obs:
                cad_obs.append(i.alumno_id)
            obj=lista_chat(chat.chat_nombre,chat.id,chat.chat_fecha_hora.strftime("%m/%d/%Y"),
                alumn_chat_editor.alumno_id,alumn_chat_mod.alumno_id,cad_obs)
            cad.append(json.loads(obj.toJSON()))

    return HttpResponse(json.dumps(cad))  