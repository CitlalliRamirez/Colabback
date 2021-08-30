from rest_framework import routers, urlpatterns
from .viewsets import AlumnoViewSet

router = routers.SimpleRouter()
router.register('alumnos', AlumnoViewSet)
urlpatterns = router.urls