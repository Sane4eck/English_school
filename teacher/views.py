from rest_framework import viewsets, status, permissions
from teacher.models import Teacher, LanguageInform
from teacher.serializer import (
    TeacherSerializer,
    LanguageInformSerializer,
    LanguageInformAllSerializer,
    TeacherAllSerializer,
)


class TeacherModelViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post"]


class TeacherAllModelViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherAllSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get"]


class LanguageInformModelViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageInformSerializer
    queryset = LanguageInform.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post"]


class LanguageInformAllModelViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageInformAllSerializer
    queryset = LanguageInform.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get"]
