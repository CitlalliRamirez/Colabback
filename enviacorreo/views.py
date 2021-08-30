from django.shortcuts import render
from django.http import HttpResponse
from usuario.models import Usuario
from django.core.mail import send_mail
# Create your views here.
def envia(request):
    correo = Usuario.objects.last().usuario_correo
    msjeid = Usuario.objects.last().id
    msjcontrasena = Usuario.objects.last().usuario_contrasena
    send_mail('Datos de registro','Tus datos han sido registrados exitosamente ID:'+str(msjeid)+' Contraseña: '+msjcontrasena,'sistemachat2@gmail.com',[correo],fail_silently=False)
    return HttpResponse("correo enviado")