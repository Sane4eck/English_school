import uuid
from datetime import timedelta, datetime
from django.db import models
from user.models import User


def time_end():
    return datetime.utcnow() + timedelta(minutes=5)  # hours=24) #TODO


class ConfirmationEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    date_finish = models.DateTimeField(default=time_end)
