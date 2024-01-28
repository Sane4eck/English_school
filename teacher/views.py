from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from urllib.parse import unquote

from english_school.settings import EMAIL_HOST_USER
from teacher.models import Teacher, LanguageInform
from teacher.serializer import TeacherSerializer, LanguageInformSerializer
from teacher.utils import TeacherRequestApprovalSender
from user.models import User


class TeacherModelViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post"]


class LanguageInformModelViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageInformSerializer
    queryset = LanguageInform.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post"]

# class LanguageInformModelViewSet(viewsets.ModelViewSet):
#     serializer_class = LanguageInformSerializer
#     queryset = LanguageInform.objects.all()
#
#     def create(self, request, *args, **kwargs):
#         instance = self.request.user
#         serializer = self.get_serializer(data=request.data, context={'user': instance})
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#
#         TeacherRequestApprovalSender(to_email=EMAIL_HOST_USER).send_email(
#             user=User.objects.get(email=instance),
#             about_teacher=AboutTeacher.objects.get(user=instance),
#             language_inform=LanguageInform.objects.get(user=instance))
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class TeacherApprovalModelViewSet(viewsets.ModelViewSet):
#     serializer_class = TeacherSerializer
#     queryset = Teacher.objects.all()
#
#     # permission_classes = permissions.IsAdminUser TODO: потом вернуть
#
#     def list(self, request, *args, **kwargs):
#         email_param = request.query_params.get('email', None)  # получаем имейл через параметры
#         decoded_email = unquote(email_param) if email_param else None  # раскодируем имейл через параметры
#
#         instance_user = User.objects.get(email=decoded_email)  # получаем конкретного пользователя через имейл
#         instance_about_teacher = AboutTeacher.objects.get(user=instance_user)  # получем данные об учителе
#         instance_language_inform = LanguageInform.objects.get(
#             user=instance_user)  # получем данные об языке преподавания
#         teacher_instance = Teacher.objects.create(user=instance_about_teacher, languages=instance_language_inform)
#
#         teacher_serializer = TeacherSerializer(teacher_instance)
#
#         return Response({"teacher_serializer": teacher_serializer.data})
