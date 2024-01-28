from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teacher.views import TeacherModelViewSet, LanguageInformModelViewSet

router = DefaultRouter()
router.register(r"about", TeacherModelViewSet, basename="Teacher")
router.register(r"language_inform", LanguageInformModelViewSet, basename="LanguageInform")
# router.register(r"teacher_approval", TeacherApprovalModelViewSet, basename="TeacherApproval")

urlpatterns = [
    path("", include(router.urls)),
]
