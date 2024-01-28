from django.urls import path, include
from rest_framework.routers import DefaultRouter
from confirmation_email.views import (
    ConfirmationEmailApiView,
    ConfirmationEmailRefreshApiView,
)

router = DefaultRouter()
router.register(r"email_status", ConfirmationEmailApiView, basename="email_status")

urlpatterns = [
    path("email_status_refresh/", ConfirmationEmailRefreshApiView.as_view()),
]
urlpatterns += router.urls
