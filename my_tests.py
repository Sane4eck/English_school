import os
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "english_school.settings")
import django

django.setup()
from user.models import User

# User.objects.all().exclude(id__in = [1,8]).delete() #удаление всех записей БД кроме
User.objects.filter(email="sanya@gmail.com").update(status_email=True)


from datetime import datetime
import time

# class MyClass:
#     dt = datetime.utcnow()
#
#     def start(self):
#         return self.dt
#
#
# class MyClass2:
#     def start(self):
#         return datetime.utcnow()
# time.sleep(5)
#
# print(MyClass().start()) #10:00:00
# print(MyClass2().start()) #10:00:05
# print(MyClass().start()) #10:00:00
# time.sleep(5)
# print(MyClass2().start()) #10:00:05
