from rest_framework import serializers

from confirmation_email.models import ConfirmationEmail
from user.models import User
from user.utils import ConfirmationEmailSender


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'second_name', 'email', 'password', 'number_phone', 'date_registration', 'gender',
                  'birthday', 'role', 'status_email']

    def create(self, validated_data):
        user_permission = self.context["request"].user
        if user_permission.is_authenticated:
            raise serializers.ValidationError("Вы уже авторизованы и не можете создать новый аккаунт.")
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        confirmation_email = ConfirmationEmail.objects.create(user=user)
        confirmation_email.save()
        ConfirmationEmailSender(to_email=user.email).send_email(user=user, email_confirmation_token=confirmation_email)
        return user
