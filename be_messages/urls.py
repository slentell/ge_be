from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, IndividualMessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='messages')
router.register(r'messages/(?P<sender>\d+)/(?P<recipient>\d+)', IndividualMessageViewSet, basename='individual_messages')

urlpatterns = router.urls