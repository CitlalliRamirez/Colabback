from rest_framework import routers, urlpatterns
from .viewsets import CursoViewSet

router = routers.SimpleRouter()
router.register('cursos', CursoViewSet)
urlpatterns = router.urls