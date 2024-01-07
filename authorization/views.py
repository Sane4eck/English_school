from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView

from user.models import User


class CustomUserAuthentication(TokenObtainPairView):
    queryset = User.objects.filter(status_email=True)

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
