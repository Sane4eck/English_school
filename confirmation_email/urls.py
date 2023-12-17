from django.urls import path

from confirmation_email.views import ConfirmationEmailApiView

urlpatterns = [
    path('email_status/<int:pk>/', ConfirmationEmailApiView.as_view(), name='confirmation_email'),
]
