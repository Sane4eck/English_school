from django.urls import path, include
from rest_framework.routers import DefaultRouter

from confirmation_email.views import ConfirmationEmailApiView, ConfirmationEmailRefreshApiView

router = DefaultRouter()
router.register(r'email_status', ConfirmationEmailApiView, basename="email_status")
# router.register(r'email_status_refresh', ConfirmationEmailRefreshApiView, basename="email_status_refresh")

urlpatterns = [
    path("", include(router.urls)),
    path("email_status_refresh/",ConfirmationEmailRefreshApiView.as_view())
]
