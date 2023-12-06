from django.core.mail import send_mail
from rest_framework import serializers
from user.models import Teacher, User
from user.utils import send_confirmation_email, greating_email


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['language', 'hourly_rate', 'status']
        verbose_name_plural = 'Teachers'


class TeacherStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['status']


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=User.ROLES, write_only=True)
    teacher = TeacherSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'name', 'second_name', 'email', 'number_phone', 'date_registration', 'gender', 'birthday',
                  'role',
                  'teacher']

    def create(self, validated_data):
        role = validated_data.pop('role', 'student')
        teacher_data = validated_data.pop('teacher', None)
        user = User.objects.create(**validated_data, role=role)

        if role == 'teacher' and teacher_data:
            teacher = Teacher.objects.create(user=user, **teacher_data)
            send_confirmation_email(user, teacher)
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['role'] = instance.get_role_display()  # Добавляем отображаемое значение роли
        return representation