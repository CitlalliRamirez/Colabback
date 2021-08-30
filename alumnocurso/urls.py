from rest_framework import routers, urlpatterns
from .viewsets import AlumnocursoViewSet

router = routers.SimpleRouter()
router.register('alumnocursos',AlumnocursoViewSet)
urlpatterns = router.urls