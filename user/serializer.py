from django.conf import settings
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.viewsets import ViewSetMixin

from user.models import Teacher, User
from user.utils import TeacherRequestEmail, VerificationEmail  # send_confirmation_email, greating_email,


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['language', 'hourly_rate', 'status']


class TeacherStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['status']


class CreateUserSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'name', 'second_name', 'email', 'password', 'number_phone', 'date_registration', 'gender',
                  'birthday', 'role', 'teacher', 'status_email', 'email_confirmation_token']

    def create(self, validated_data):
        user = self.context["request"].user
        if user.is_authenticated:
            raise serializers.ValidationError("Вы уже авторизованы и не можете создать новый аккаунт.")
        teacher_data = validated_data.pop("teacher", None)
        user = User.objects.create(**validated_data)
        VerificationEmail(to_email=user.email).send_email(user=user)
        if user.role == "teacher" and teacher_data:
            teacher = Teacher.objects.create(user=user, **teacher_data)
            TeacherRequestEmail(to_email=settings.EMAIL_BOSS).send_email(user=user, teacher=teacher)
        return user
