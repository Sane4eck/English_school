import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "english_school.settings")
import django

django.setup()

from user.utils import greating_email

greating_email()
