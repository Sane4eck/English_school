from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserApiViewSet, TeacherStatusUpdateView


router = DefaultRouter()
router.register(r'users', UserApiViewSet, basename ='UserApiView')

urlpatterns = [
    path('',include(router.urls)),
    path('update-teacher-status/<int:pk>/', TeacherStatusUpdateView.as_view(), name='update-teacher-status'),
]
