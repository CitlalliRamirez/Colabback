from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [path('',views.listadocurso, name='index'),
               path('/listadochat',views.listadochat,name='listadochat'),
               path('/listadogrupo',views.listadogrupo, name='listadogrupo')] 
