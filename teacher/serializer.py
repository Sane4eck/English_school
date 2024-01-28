from rest_framework import serializers

from teacher.models import Teacher, LanguageInform


class TeacherSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return Teacher.objects.create(**validated_data)

    class Meta:
        model = Teacher
        fields = ["about_teacher"]


class LanguageInformSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        teacher = Teacher.objects.get(user=user)
        validated_data['teacher'] = teacher
        return LanguageInform.objects.create(**validated_data)

    class Meta:
        model = LanguageInform
        fields = ["language", "cost", "experience_language"]

# class LanguageInformSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LanguageInform
#         fields = ["language", "cost", "status_language", "experience_language", "date_approval_language"]
#
#     def create(self, validated_data):
#         user = self.context["user"]
#         validated_data["user"] = user  # Добавляем пользователя в словарь
#         language_inform_instance = LanguageInform.objects.create(**validated_data)
#         return language_inform_instance
#
#
# class TeacherSerializer(serializers.ModelSerializer):
#     # about_teacher = AboutTeacherSerializer()
#     # languages = LanguageInformSerializer()
#
#     class Meta:
#         model = Teacher
#         fields = ["user", "languages"]


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class AboutTeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AboutTeacher
#         fields = '__all__'
#
# class LanguageInformSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LanguageInform
#         fields = '__all__'
