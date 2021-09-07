"""colabback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('backtablas/', include('usuario.urls')),
    path('backtablas/', include('administrador.urls')),
    path('backtablas/', include('profesor.urls')),
    path('backtablas/', include('alumno.urls')),
    path('backtablas/', include('curso.urls')),
    path('backtablas/', include('chat.urls')),
    path('backtablas/autentificar', include('authtoken.urls')),
    path('backtablas/', include('alumnocurso.urls')),
    path('backtablas/', include('alumnochat.urls')),
    path('backtablas/guarda', include('guardacurso.urls')),
    path('backtablas/listado', include('listausuario.urls')),
    path('backtablas/listadocurso', include('listacurso.urls')),
    path('backtablas/envia', include('enviacorreo.urls')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
