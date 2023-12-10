from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def __base_send_email(email: str, html: str, subject: str):
    msg = EmailMessage(
        subject=subject,
        body=html.replace("\n", ""),
        from_email=settings.EMAIL_SENDER,
        to=[email],
    )
    msg.content_subtype = "html"
    msg.send()


def send_confirmation_email(user, teacher):
    html = render_to_string(
        "email/confirmation_teacher.html",
        {
            "username": user.name,
            "second_name": user.second_name,
            "email": user.email,
            "number_phone": user.number_phone,
            "gender": user.gender,
            "birthday": user.birthday,
            "role": user.role,
            "language": teacher.language,
            "hourly_rate": teacher.hourly_rate,
            "reset_url": f"http://127.0.0.1:8000/admin/user/teacher/{user.id}/change/",  # замінити на посиланя urls
        },
    )
    __base_send_email(
        "alexsan4es619@gmail.com",
        # "o.s.cherniavskyi@gmail.com",
        html,
        "English_site",
    )


def greating_email():  # user:  User verify_email):
    """
    for test.py
    """
    html = render_to_string(
        "email/confirmation_teacher.html",
        {
            "username": "Sashko",
            "email": "alexsan4es619@gmail.com",
            "reset_url": f"",
        },
    )
    __base_send_email(
        "alexsan4es619@gmail.com",
        html,
        "Welcome to Bongit!",
    )
