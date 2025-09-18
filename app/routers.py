from rest_framework import routers
from .views import StudentViewSet


router = routers.DefaultRouter()
router.register(r'Student', StudentViewSet)

urlpatterns = router.urls