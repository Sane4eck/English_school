from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserApiViewSet

router = DefaultRouter()
router.register(r"", UserApiViewSet, basename="UserApiView")

urlpatterns = []

urlpatterns += router.urls
