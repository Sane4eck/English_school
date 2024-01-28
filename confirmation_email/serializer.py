from rest_framework import serializers
from confirmation_email.models import ConfirmationEmail
from user.models import User


class ConfirmationEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmationEmail
        fields = ["id", "email_confirmation_token", "date_finish"]


class ConfirmationEmailRefreshSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "status_email",
        ]
