from rest_framework import routers, urlpatterns
from .viewsets import AdministradorViewSet

router = routers.SimpleRouter()
router.register('administradores', AdministradorViewSet)
urlpatterns = router.urls