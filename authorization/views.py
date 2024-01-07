from rest_framework import generics
from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from user.models import User


# class CustomUserAuthentication(BaseAuthentication):
#     queryset = User.objects.filter(status_email=True)
#     def authenticate(self, request):
#         # Получаем токен из запроса (или None, если токена нет)
#         token = JWTAuthentication().get_validated_token(request)
#
#         # Получаем пользователя из токена
#         user = JWTAuthentication().get_user(token)
#
#         # Проверяем, что пользователь активен и status_email равен True
#         if user and user.is_active and user.status_email:
#             return user, None
#         else:
#             raise AuthenticationFailed('Invalid authentication credentials')

class CustomUserAuthentication(TokenObtainPairView):
    queryset = User.objects.filter(status_email=True)
    # def post(self, request, *args, **kwargs):
    #     self.queryset = User.objects.filter(status_email=True)
    #     return super().post(request, *args, **kwargs)
    # def get_queryset(self):
    #     return User.objects.filter(status_email=True)
    # queryset = User.objects.filter(status_email=True)
    # print(queryset)

# class CustomUserAuthentication(JWTAuthentication):
#     def authenticate(self, request):
#         if request.path == "/api/v1/user-registration/":
#             return None
#         if "/confirmation_email/email_status/" in request.path:
#             return None
#             # параметр 'status_email' равен 'approved'
#             # if request.GET.get('status_email') == 'approved':
#             #     return None
#         user, jwt_value = super().authenticate(request)
#
#         if user and hasattr(user, "status_email"):
#             status_email = getattr(user, "status_email")
#             if status_email == "pending":
#                 raise AuthenticationFailed("Вы еще не подтвердили свой email...")
#
#         if user and hasattr(user, "teacher"):
#             teacher_status = getattr(user.teacher, "status", None)
#
#             if teacher_status == "rejected":
#                 raise AuthenticationFailed("Вам запрещен доступ. Ваш статус: 'Rejected'.")
#             elif teacher_status == "pending":
#                 raise AuthenticationFailed(
#                     "Ожидайте, пока администраторы проверят Ваши данные и предоставят доступ. Ваш статус: 'Pending'.")
#
#         return user, jwt_value
