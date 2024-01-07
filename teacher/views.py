# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser
#
# from teacher.models import Teacher
#
#
# class TeacherApiViewSet(generics.UpdateAPIView, generics.RetrieveAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherStatusUpdateSerializer
#     permission_classes = [IsAdminUser]
#     http_method_names = ["patch"]


# class TeacherStatusUpdateView(generics.UpdateAPIView, generics.RetrieveAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherStatusUpdateSerializer
#     permission_classes = [IsAdminUser]
#     http_method_names = ["patch"]
