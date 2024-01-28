from user.utils import EmailSender
from urllib.parse import quote

class TeacherRequestApprovalSender(EmailSender):
    email = "email/confirmation_teacher.html"
    subject = "English_site"

    def generate_context(self, **kwargs):
        user = kwargs["user"]
        about_teacher = kwargs["about_teacher"]
        language_inform = kwargs["language_inform"]
        quote_email = quote(user.email)

        return {
            "username": user.name,
            "second_name": user.second_name,
            "email": user.email,
            "number_phone": user.number_phone,
            "date_registration": user.date_registration,
            "gender": user.gender,
            "birthday": user.birthday,
            "role": user.role,

            "about_teacher": about_teacher.about_teacher,

            "language": language_inform.language,
            "cost": language_inform.cost,
            "experience_language": language_inform.experience_language,

            "reset_url": f"http://127.0.0.1:8000/api/teacher/teacher_approval/?email={quote_email}",
        }