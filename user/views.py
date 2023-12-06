from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from user.models import User, Teacher
from user.serializer import UserSerializer, TeacherStatusUpdateSerializer
from user.utils import send_confirmation_email


class UserApiView(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()#.order_by("email")
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        else:
            return []  # IsAdminUser()]


class TeacherStatusUpdateView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherStatusUpdateSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # send_confirmation_email("o.s.cherniavskyi@gmail.com", serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
