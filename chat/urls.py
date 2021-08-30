from rest_framework import routers, urlpatterns
from .viewsets import ChatViewSet

router = routers.SimpleRouter()
router.register('chats', ChatViewSet)
urlpatterns = router.urls