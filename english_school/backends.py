from django.contrib.auth.backends import ModelBackend


class CheckAccessBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        user = super().authenticate(request, **kwargs)
        if user and user.status_email == True:
            return user
