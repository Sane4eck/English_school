from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class EmailSender:
    def __init__(self, to_email):
        self.to_email = to_email

    email = ""
    subject = ""

    def generate_context(self, **kwargs):
        return {}

    def __send_email(self, to_email, subject, html_body):
        msg = EmailMessage(
            subject=subject,
            body=html_body.replace("\n", ""),
            from_email=settings.EMAIL_SENDER,
            to=[to_email],
        )
        msg.content_subtype = "html"
        msg.send()

    def send_email(self, **kwargs):
        # print(kwargs['email'])
        html = render_to_string(
            self.email,
            self.generate_context(**kwargs),
        )
        self.__send_email(self.to_email, self.subject, html)


class ConfirmationEmailSender(EmailSender):
    email = "email/confirmation_email.html"
    subject = "English_site"

    def generate_context(self, **kwargs):
        user = kwargs["user"]
        email_confirmation_token_model = kwargs["email_confirmation_token"]
        return {
            "username": user.name,
            "verification_url": f"http://127.0.0.1:8000/api/confirmation_email/email_status/{email_confirmation_token_model.email_confirmation_token}/",
        }
