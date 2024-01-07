# from django.db import models
# from user.models import User
#
#
# class Teacher(models.Model):
#     class StatusTeacher(models.TextChoices):
#         PENDING = "pending", "Pending"
#         APPROVED = "approved", "Approved"
#         REJECTED = "rejected", "Rejected"
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.CharField("Teacher Status", choices=StatusTeacher.choices, default=StatusTeacher.PENDING,
#                               max_length=10)
#
#
# class Languages(models.Model):
#     class LanguageChoices(models.TextChoices):
#         ENGLISH = "English", "English"
#         GERMAN = "German", "German"
#         FRENCH = "French", "French"
#         UKRAINIAN = "Ukrainian", "Ukrainian"
#         POLISH = "Polish", "Polish"
#
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     language = models.CharField("Teaching Language", choices=LanguageChoices.choices, max_length=15)
#     hourly_rate = models.DecimalField("Hourly Rate", max_digits=5, decimal_places=2)
