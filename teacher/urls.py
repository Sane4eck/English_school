from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teacher.views import (
    TeacherModelViewSet,
    LanguageInformModelViewSet,
    LanguageInformAllModelViewSet,
    TeacherAllModelViewSet,
)

router = DefaultRouter()
router.register(r"about/all", TeacherAllModelViewSet, basename="TeacherAll")
router.register(r"about", TeacherModelViewSet, basename="Teacher")
router.register(
    r"language_inform/all", LanguageInformAllModelViewSet, basename="LanguageInformAll"
)
router.register(
    r"language_inform", LanguageInformModelViewSet, basename="LanguageInform"
)

urlpatterns = []  # path("", include(router.urls)),
urlpatterns += router.urls
