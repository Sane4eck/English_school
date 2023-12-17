import uuid

from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from confirmation_email.serializer import ConfirmationEmailSerializer
from user.models import User
from rest_framework.response import Response
from rest_framework import status


class ConfirmationEmailApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ConfirmationEmailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        email_confirmation_token = uuid.UUID(request.query_params.get("email_confirmation_token", None))
        status_email = request.query_params.get("status_email", None)
        instance = self.get_object()
        if email_confirmation_token and status_email:
            if instance.status_email == "approved":
                return Response({"detail": "Статус email уже был подтверждён."}, status=status.HTTP_400_BAD_REQUEST)
            elif instance.status_email == "pending":
                if instance.email_confirmation_token == email_confirmation_token:
                    instance.status_email = status_email
                    instance.save()
                    return Response({"detail": "email успешно подтверждён."}, status=status.HTTP_200_OK)
        return Response({"detail": "Неверный токен или статус email."}, status=status.HTTP_400_BAD_REQUEST)
