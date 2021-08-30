from rest_framework import routers, urlpatterns
from .viewsets import ProfesorViewSet

router = routers.SimpleRouter()
router.register('profesores', ProfesorViewSet)
urlpatterns = router.urls