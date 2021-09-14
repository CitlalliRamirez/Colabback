from django.shortcuts import render
from django.http import HttpResponse
from usuario.models import Usuario
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt 
def envia(request): 
    if request.method=='POST':
        correo = request.POST.get("correo")#Usuario.objects.last().usuario_correo
        msjeid = request.POST.get("idU") #Usuario.objects.last().id
        msjcontrasena = request.POST.get("contrasena")#Usuario.objects.last().usuario_contrasena
        mensaje = request.POST.get("mensaje")
        send_mail('Datos de registro','Tus datos han sido '+mensaje+' exitosamente ID:'+str(msjeid)+' Contraseña: '+msjcontrasena,'sistemachat2@gmail.com',[correo],fail_silently=False)
    return HttpResponse("correo enviado")