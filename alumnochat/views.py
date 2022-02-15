from django.http.response import HttpResponse
from django.shortcuts import render
from alumnocurso.models import Alumnocurso
from alumno.models import Alumno
from profesor.models import Profesor
from curso.models import Curso
from chat.models import Chat
from alumnochat.models import Alumnochat
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

class lista_alum_curso():
    def __init__(self,id,nombre):
        self.nombre = nombre
        self.id = id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# Create your views here.
class lista_alum_chat():
    def __init__(self,id,nombre):
        self.nombre = nombre
        self.id = id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def jsonDefault(object):
    return object.__dict__

@csrf_exempt
def listaAlumnos(request):
    cad = []
    data= None
    if request.method=='POST':
        idcurso = request.POST.get('id')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        alum_en_chat =[]#todos los alumnos que estan en chats de ese curso que coinciden en hora y fecha
        idalumnos = Alumnocurso.objects.filter(curso_id=idcurso)#alumnos de ese curso
        chatscurso = Chat.objects.filter(chat_fecha=fecha,chat_hora=hora)# chats que coincida con la fecha y hora que se quiere registrar otro chat  
        for i in chatscurso:
            alumno_por_chat= Alumnochat.objects.filter(chat_id=i.id)
            for j in alumno_por_chat:
                alum_en_chat.append(j.alumno_id)
        for idal in idalumnos:
            if idal.alumno_id not in alum_en_chat:
                nombre = Alumno.objects.filter(id=idal.alumno_id)[0]
                obj = lista_alum_curso(idal.alumno_id,nombre.alumno_nombre)
                cad.append(json.loads(obj.toJSON()))
    return HttpResponse(json.dumps(cad))
 

@csrf_exempt
def guardaC(request):
    data = "ok"
    if request.method=='POST':
        id = request.POST.get('idcurso')
        nombre = request.POST.get('nombre')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        editor = request.POST.get('editor')
        moderador = request.POST.get('moderador')
        observadores = request.POST.get('observadores')
        idprofesor = Curso.objects.filter(id=id)[0].profesor.id
        obs = observadores.split(',')
        respaldo = [] #guarda mis alumnos a guardar en el nuevo chat
        cont = 0
        respaldo.append(editor)
        respaldo.append(moderador)
        for i in obs:
            respaldo.append(i)
        alum_en_chat =[] #alumnos que estén en chats a la misma hora y fecha
        #revisar si ya hay un chat a esa hora y fecha
        result = Chat.objects.filter(chat_fecha=fecha,chat_hora=hora)
        if(result.count()==0):
            Chat.objects.create(chat_nombre=nombre,chat_conversacion='',chat_fecha=fecha,chat_hora=hora,profesor_id=idprofesor,curso_id=id)
            idchat = Chat.objects.last().id
            Alumnochat.objects.create(rol='Editor',chat_id=idchat,alumno_id=editor)
            Alumnochat.objects.create(rol='Moderador',chat_id=idchat,alumno_id=moderador)
            for i in obs:
                Alumnochat.objects.create(rol='Observador',chat_id=idchat,alumno_id=i)
        if(result.count()>=1): #si hay uno o mas, entonces se tiene que revisar que alumnos estan en esos chats y si coincide con uno de estos alumnos, no generar chat
           for i in result:
               alumno_por_chat= Alumnochat.objects.filter(chat_id=i.id)
               for j in alumno_por_chat:
                    alum_en_chat.append(j.alumno_id)
           for i in respaldo:#itero mis alumnos a guardar
               if i in alum_en_chat:
                   cont= cont+1
           if cont==0: #si no coindicen los alumnos, generar chat
                Chat.objects.create(chat_nombre=nombre,chat_conversacion='',chat_fecha=fecha,chat_hora=hora,profesor_id=idprofesor,curso_id=id)
                idchat = Chat.objects.last().id
                Alumnochat.objects.create(rol='Editor',chat_id=idchat,alumno_id=editor)
                Alumnochat.objects.create(rol='Moderador',chat_id=idchat,alumno_id=moderador)
                for i in obs:
                    Alumnochat.objects.create(rol='Observador',chat_id=idchat,alumno_id=i)
        
       
    return HttpResponse(data)

@csrf_exempt
def listaAlumnosEditar(request):
    cad = []
    data= None
    if request.method=='POST':
        idchat= int(request.POST.get('id'))
        idcurso = Chat.objects.filter(id=idchat)[0].curso_id
        alum_en_chat =[]#
        fecha = request.POST.get('fecha')#"2021-12-06"
        hora= request.POST.get('hora')#"08:00:00"
        idalumnos = Alumnocurso.objects.filter(curso_id=idcurso)#alumnos de ese curso
        chatscurso = Chat.objects.filter(chat_fecha=fecha,chat_hora=hora)# todos los chats que estén en la misma hora y fecha al editable
        for i in chatscurso:
            if i.id!=idchat:
                alumno_por_chat= Alumnochat.objects.filter(chat_id=i.id)
                for j in alumno_por_chat:
                    alum_en_chat.append(j.alumno_id)
        for idal in idalumnos:
            if idal.alumno_id not in alum_en_chat:
                nombre = Alumno.objects.filter(id=idal.alumno_id)[0]
                obj = lista_alum_chat(idal.alumno_id,nombre.alumno_nombre)
                cad.append(json.loads(obj.toJSON()))
    return HttpResponse(json.dumps(cad))

@csrf_exempt
def actualizarC(request):
    data = "ok"
    if request.method=='POST': 
        idchat = request.POST.get('id')
        nombre = request.POST.get('nombre')
        editor = request.POST.get('editor')
        moderador = request.POST.get('moderador')
        observadores = request.POST.get('observadores')
        obs = observadores.split(',')
        Chat.objects.filter(pk=idchat).update(chat_nombre=nombre)
        Alumnochat.objects.filter(chat_id=idchat).delete()
        Alumnochat.objects.create(rol='Editor',chat_id=idchat,alumno_id=editor)
        Alumnochat.objects.create(rol='Moderador',chat_id=idchat,alumno_id=moderador)
        for i in obs:
            Alumnochat.objects.create(rol='Observador',chat_id=idchat,alumno_id=i)
        
       
    return HttpResponse(data)

@csrf_exempt
def existecurso(request):
    data=None
    if request.method=='POST':
        semestre = request.POST.get("semestre")
        carrera = request.POST.get("carrera")
        num = Alumno.objects.filter(alumno_semestre=semestre,alumno_carrera=carrera).count()
        if num>0:
            idd = Alumno.objects.filter(alumno_semestre=semestre,alumno_carrera=carrera).last().id
            numac = Alumnocurso.objects.filter(alumno_id=idd).count()
            if numac>0:
                data = Alumnocurso.objects.filter(alumno_id=idd)[0].curso_id
            else:
                data=0
        else:
            data=0
    return HttpResponse(data)

@csrf_exempt
def insertacurso(request):
    data=None
    if request.method=='POST':
        idcurso = int(request.POST.get("idcurso"))
        id  = int(request.POST.get("id"))
        if idcurso>0:
            #insertar a alumnocurso
            Alumnocurso.objects.create(curso_id=idcurso,alumno_id=id)
            data='si'
        else:
            data='no'
    return HttpResponse(data)

@csrf_exempt
def rol(request):
    data=None
    if request.method=='POST':
        id = int(request.POST.get("id"))
        rol = Alumnochat.objects.filter(alumno_id=id)[0].rol
        data=rol
    return HttpResponse(data)
