from requests import Response
from rest_framework import serializers, status

from confirmation_email.models import ConfirmationEmail
from user.models import User


class ConfirmationEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmationEmail
        fields = ["id", "email_confirmation_token", "date_finish"]


class ConfirmationEmailRefreshSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'status_email']  # ["id", "email_confirmation_token", "date_create_token"]

    # def get(self, request, *args, **kwargs):
    #     param_value = request.query_params.get('email')#.filters(status_email=True)
    #     print("param_value")
    #     return Response({"email": param_value})

    # def to_representation(self, instance):

    # def create(self, request, *args, **kwargs):
    #     email = kwargs["email"]
    #     print(email)
    #     # serializer = self.get_serializer(data=request.data)
    #     # serializer.is_valid(raise_exception=True)
    #     # self.perform_create(serializer)
    #     # headers = self.get_success_headers(serializer.data)
    #     # print(serializer)
