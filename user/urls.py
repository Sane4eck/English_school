from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserApiViewSet

router = DefaultRouter()
router.register(r'user', UserApiViewSet, basename='UserApiView')

urlpatterns = [
    path('', include(router.urls)),
]
