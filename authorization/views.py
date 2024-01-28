from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User


class CustomUserAuthentication(TokenObtainPairView):
    queryset = User.objects.filter(status_email=True)
