import uuid
from datetime import datetime

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


class ConfirmationEmailApiView(RetrieveModelMixin, GenericViewSet):
    def get_queryset(self):
        return ConfirmationEmail.objects.filter(date_finish__gt=datetime.utcnow())

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
        try:
            instance = User.objects.get(email=json_data["email"])
        except User.DoesNotExist:
            return Response({"There is no such email": status.HTTP_204_NO_CONTENT})
        if instance.status_email == True:
            return Response({"Email already confirmed": status.HTTP_200_OK})
        elif instance.status_email == False:
            try:
                confirmation_email = ConfirmationEmail.objects.get(user_id=instance.id)
                if confirmation_email.date_finish < datetime.utcnow():
                    confirmation_email.delete()
                    confirmation_email = ConfirmationEmail.objects.create(user=instance)
                    confirmation_email.save()
                    ConfirmationEmailSender(to_email=instance.email).send_email(user=instance,
                                                                            email_confirmation_token=confirmation_email)
                else:
                    return Response({"The letter is already in your mail, check your spam": status.HTTP_200_OK})
                return Response({"A letter has been sent by mail": status.HTTP_200_OK})
            except ConfirmationEmail.DoesNotExist:
                return Response({"Contact support!": status.HTTP_200_OK})
