import uuid
from datetime import datetime, timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from confirmation_email.models import ConfirmationEmail
from confirmation_email.serializer import ConfirmationEmailSerializer, ConfirmationEmailRefreshSerializer
from rest_framework.response import Response

from user.models import User
from user.serializer import UserSerializer
from user.utils import ConfirmationEmailSender

def time():
    return datetime.utcnow()

class ConfirmationEmailApiView(RetrieveModelMixin, GenericViewSet):
    def get_queryset(self):
        return ConfirmationEmail.objects.filter(date_finish__gt=timezone.now())

    serializer_class = ConfirmationEmailSerializer
    permission_classes = [AllowAny]
    lookup_field = "email_confirmation_token"  # изменения ретрив параметра

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.status_email = True
        instance.user.save()
        instance.delete()
        return Response({"status": True})


class ConfirmationEmailRefreshApiView(CreateModelMixin, GenericAPIView):
    serializer_class = ConfirmationEmailRefreshSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        json_data = request.data
        instance = User.objects.filter(email=json_data["email"]).first()
        if not instance:
            return Response({"There is no such email": status.HTTP_404_NOT_FOUND})
        if instance.status_email:
            return Response({"Email already confirmed": status.HTTP_200_OK})
        else:
            confirmation_email, created = ConfirmationEmail.objects.get_or_create(user_id=instance.id, defaults={})
            if confirmation_email.date_finish < timezone.now():
                print(timezone.now())
                confirmation_email.delete()
                confirmation_email = ConfirmationEmail.objects.create(user=instance)
                confirmation_email.save()
                ConfirmationEmailSender(to_email=instance.email).send_email(user=instance,
                                                                        email_confirmation_token=confirmation_email)
            else:
                print(timezone.now())
                return Response({"The letter is already in your mail, check your spam": status.HTTP_200_OK})
            return Response({"A letter has been sent by mail": status.HTTP_200_OK})
