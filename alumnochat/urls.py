from rest_framework import routers, urlpatterns
from .viewsets import AlumnochatViewSet

router = routers.SimpleRouter()
router.register('alumnochats',AlumnochatViewSet)
urlpatterns = router.urls