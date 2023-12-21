from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser

from rest_framework import viewsets

from user.models import User, Teacher
from user.serializer import TeacherStatusUpdateSerializer, CreateUserSerializer


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [permissions.AllowAny]
        elif self.action == "partial_update":
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action in ["list", "retrieve", "update", "destroy"]:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


# class UserCreateApiView(generics.CreateAPIView):
#     """
#       Создание пользователя
#     """
#     queryset = User.objects.all()  # .order_by("email")
#     serializer_class = CreateUserSerializer
#     permission_classes = [AllowAny]


class TeacherStatusUpdateView(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherStatusUpdateSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ["patch"]
