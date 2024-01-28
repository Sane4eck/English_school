from rest_framework import permissions
from rest_framework import viewsets
from user.models import User
from user.serializer import UserSerializer


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [permissions.AllowAny, ]
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
