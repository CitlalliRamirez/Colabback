from django.shortcuts import render
from django.http import HttpResponse
from usuario.models import Usuario
from alumno.models import Alumno
from administrador.models import Administrador
from profesor.models import Profesor
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import jwt
# Create your views here.
@csrf_exempt
def autentificar(request):
    data = None
    if request.method=='POST':
        pas = request.POST.get('contrasena')
        id = request.POST.get('id')
        res = Usuario.objects.filter(id=id,usuario_contrasena=pas).count()
        key = "secret"
        if res!=0:
            num_al = Alumno.objects.filter(usuario=id).count()
            num_pr = Profesor.objects.filter(usuario=id).count()
            num_ad = Administrador.objects.filter(usuario=id).count()
            if num_al!=0:
                dat_al = Alumno.objects.filter(usuario=id)[0]
                encoded = jwt.encode({"Tipo": "Alumno","Nombre":dat_al.alumno_nombre,"Id":dat_al.id}, key, algorithm="HS256")
                data=encoded
            elif num_pr!=0:
                dat_pr = Profesor.objects.filter(usuario=id)[0]
                encoded = jwt.encode({"Tipo": "Profesor","Nombre":dat_pr.profesor_nombre,"Id":dat_pr.id}, key, algorithm="HS256")
                data=encoded
            elif num_ad!=0:
                dat_ad = Administrador.objects.filter(usuario=id)[0]
                encoded = jwt.encode({"Tipo": "Administrador","Nombre":dat_ad.administrador_nombre,"Id":dat_ad.id}, key, algorithm="HS256")
                data=encoded
            else:
                data=-1
        else:
            data=0
        
            
    return HttpResponse(data)
