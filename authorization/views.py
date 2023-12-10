from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomUserAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Вызываем родительский метод authenticate для получения пользователя из токена
        user, jwt_value = super().authenticate(request)

        if user and hasattr(user, "status_email"):
            status_email = getattr(user, "status_email")
            if status_email == "pending":
                raise AuthenticationFailed("Вы еще не подтвердили свой email...")

        if user and hasattr(user, "teacher"):
            teacher_status = getattr(user.teacher, "status", None)

            if teacher_status == "rejected":
                raise AuthenticationFailed("Вам запрещен доступ. Ваш статус: 'Rejected'.")
            elif teacher_status == "pending":
                raise AuthenticationFailed(
                    "Ожидайте, пока администраторы проверят Ваши данные и предоставят доступ. Ваш статус: 'Pending'.")
        # else:
        #     raise AuthenticationFailed("Вам запрещен доступ. Неверные учетные данные.")

        return user, jwt_value
