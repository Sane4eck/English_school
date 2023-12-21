from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authorization.views import CustomUserAuthentication

# from authorization.views import ConfirmationEmailApiView

urlpatterns = [
    path('token/', CustomUserAuthentication.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
