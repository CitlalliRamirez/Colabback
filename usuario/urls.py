from rest_framework import routers, urlpatterns
from .viewsets import UsuarioViewSet

router = routers.SimpleRouter()
router.register('usuarios', UsuarioViewSet)
urlpatterns = router.urls