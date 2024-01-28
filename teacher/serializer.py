from rest_framework import serializers

from english_school.settings import EMAIL_HOST_USER
from teacher.models import Teacher, LanguageInform
from teacher.utils import TeacherRequestApprovalSender


class TeacherSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return Teacher.objects.create(**validated_data)

    class Meta:
        model = Teacher
        fields = ["about_teacher"]


class LanguageInformSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context["request"].user
        teacher = Teacher.objects.get(user=user)
        validated_data["teacher"] = teacher
        language_inform = LanguageInform.objects.create(**validated_data)
        TeacherRequestApprovalSender(to_email=EMAIL_HOST_USER).send_email(
            language_inform=language_inform
        )
        return language_inform

    class Meta:
        model = LanguageInform
        fields = ["language", "cost", "experience_language"]


class TeacherAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class LanguageInformAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageInform
        fields = "__all__"
