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

@csrf_exempt     
def listadocurso(request):
    cad = []
    data=''
    if request.method=='POST':
        idTipo = request.POST.get('tipo')
        idU =   request.POST.get('idU')
        if idTipo=="Alumno":
            AC = Alumnocurso.objects.filter(alumno_id=idU)
            for i in AC:
                curso = Curso.objects.filter(id=i.curso.id)[0]
                datosAlum = Alumno.objects.filter(id=idU)
                obj = lista_cursos(curso.curso_nombre, datosAlum[0].alumno_semestre,curso.id,datosAlum[0].alumno_carrera,curso.profesor.id)
                cad.append(json.loads(obj.toJSON()))      
        else:
            if idTipo=="Profesor":#si es profesor
                data="pro"
                cursos = Curso.objects.filter(profesor_id=idU)
            else:
                cursos = Curso.objects.all()
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
    def __init__(self,nombre,id,fecha,hora,editor,moderador,observador):
        self.nombre = nombre
        self.id = id
        self.fecha = fecha
        self.hora = hora
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
    data=None
    if request.method=='POST':
        idcurso = request.POST.get('id')
        Tipo= request.POST.get('tipo')
        idU =int(request.POST.get('idU'))
        if Tipo=="Alumno":
            chats=Chat.objects.filter(curso_id=idcurso)
            for chat in chats:
                Num= Alumnochat.objects.filter(chat_id=chat.id,alumno_id=idU).count()
                if Num!=0:
                    idUU =Alumnochat.objects.filter(chat_id=chat.id,alumno_id=idU)[0]
                    if idUU.alumno_id ==idU:
                        cad_obs=[]
                        alumn_chat_editor = Alumnochat.objects.filter(chat_id=chat.id,rol='Editor')[0]
                        alumn_chat_mod = Alumnochat.objects.filter(chat_id=chat.id,rol='Moderador')[0]
                        alumn_chat_obs = Alumnochat.objects.filter(chat_id=chat.id,rol='Observador')
                        for i in alumn_chat_obs:
                            cad_obs.append(i.alumno_id)
                        obj=lista_chat(chat.chat_nombre,chat.id,chat.chat_fecha,str(chat.chat_hora),
                            alumn_chat_editor.alumno_id,alumn_chat_mod.alumno_id,cad_obs)
                        cad.append(json.loads(obj.toJSON()))

        else:
            chats=Chat.objects.filter(curso_id=idcurso)
            for chat in chats:
                cad_obs=[]
                alumn_chat_editor = Alumnochat.objects.filter(chat_id=chat.id,rol='Editor')[0]
                alumn_chat_mod = Alumnochat.objects.filter(chat_id=chat.id,rol='Moderador')[0]
                alumn_chat_obs = Alumnochat.objects.filter(chat_id=chat.id,rol='Observador')
                for i in alumn_chat_obs:
                    cad_obs.append(i.alumno_id)
                obj=lista_chat(chat.chat_nombre,chat.id,chat.chat_fecha,str(chat.chat_hora),
                    alumn_chat_editor.alumno_id,alumn_chat_mod.alumno_id,cad_obs)
                cad.append(json.loads(obj.toJSON()))

    return HttpResponse(json.dumps(cad))

#listar los chats
class lista_grupo():
    def __init__(self,nombre):
        self.nombre = nombre
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# Create your views here.
def jsonDefault(object):
    return object.__dict__

@csrf_exempt     
def listadogrupo(request):
    cad = []
    data='ok'
    if request.method=='POST':
        carrera = request.POST.get("carrera")
        semestre = request.POST.get("semestre")
        lista = Alumno.objects.filter(alumno_semestre=semestre,alumno_carrera=carrera)
        for i in lista:
            obj = lista_grupo(i.alumno_nombre)
            cad.append(json.loads(obj.toJSON()))
    return HttpResponse(json.dumps(cad)) 