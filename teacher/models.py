from django.db import models
from user.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_teacher = models.TextField(verbose_name="About me", blank=False)


class LanguageInform(models.Model):
    class LanguageChoices(models.TextChoices):
        ENGLISH = "English", "English"
        GERMAN = "German", "German"
        FRENCH = "French", "French"
        UKRAINIAN = "Ukrainian", "Ukrainian"
        POLISH = "Polish", "Polish"

    class StatusLanguageChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    class ExperienceTeachingChoices(models.TextChoices):
        LESSYEAR = "lessyear", "less than a year"
        ONEYEAR = "oneyear", "one year"
        TWOYEARS = "twoyears", "two years"
        THREEYEARS = "threeyears", "two - three years"
        FIVEYEARS = "fiveyears", "three - five years"
        TENYEARS = "tenyears", "five - ten years"
        MORETENYEARS = "moretenyears", "more than ten years"

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="languages")
    language = models.CharField("Teaching Language", choices=LanguageChoices.choices, max_length=15)
    cost = models.FloatField("Cost")
    experience_language = models.CharField("Experience teaching language", choices=ExperienceTeachingChoices,
                                           max_length=20)
    status_language = models.CharField("Status language", choices=StatusLanguageChoices.choices, max_length=10,
                                       default=StatusLanguageChoices.PENDING)
    date_approval_language = models.DateTimeField(null=True)
