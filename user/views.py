from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from user.models import User, Teacher
from user.serializer import UserSerializer, TeacherStatusUpdateSerializer, CreateUserSerializer


class UserApiView(generics.ListAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()  # .order_by("email")
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticated]


class UserCreateApiView(generics.CreateAPIView):
    """
      Создание пользователя
    """
    queryset = User.objects.all()  # .order_by("email")
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        password = data.get('password')
        hashed_password = make_password(password)
        data['password'] = hashed_password
        response = super().create(request, *args, **kwargs)
        return response


class TeacherStatusUpdateView(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherStatusUpdateSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
