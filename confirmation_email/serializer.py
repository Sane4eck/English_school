from rest_framework import serializers

from user.models import User


class ConfirmationEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "status_email", "email_confirmation_token"]
