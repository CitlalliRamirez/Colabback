from rest_framework import routers, urlpatterns
from django.urls import path
from django.conf.urls import include
from .viewsets import AlumnochatViewSet
from . import views

router = routers.SimpleRouter()
router.register('alumnochats',AlumnochatViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('lista',views.listaAlumnos, name='lista'),
    path('guardac',views.guardaC, name='guardac'),
    path('listae',views.listaAlumnosEditar,name='listae'),
    path('actualizarc',views.actualizarC,name='actualizarc')
]
