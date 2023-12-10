from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)  # Добавь эту строку
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    GENDERS = (
        ("m", "Male"),
        ("f", "Female")
    )
    ROLES = (
        ("teacher", "Teacher"),
        ("student", "Student")
    )
    STATUS_EMAIL_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    )
    name = models.CharField("First Name", max_length=30, )
    # password = models.CharField("Password", max_length=15, blank=True)
    second_name = models.CharField("Second Name", max_length=30)
    email = models.EmailField("Email", unique=True)
    number_phone = models.CharField("Number_phone", max_length=10, unique=True)
    date_registration = models.DateField(auto_now_add=True)
    gender = models.CharField("Gender", choices=GENDERS, max_length=1)
    birthday = models.DateField("Birthday", blank=True)
    role = models.CharField("Role", choices=ROLES, max_length=7, default='student')
    status_email = models.CharField("Status_email",choices=STATUS_EMAIL_CHOICES,max_length=8, default="pending")

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "second_name", "birthday", "number_phone", "gender", "role"]

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return f"{self.name} {self.second_name}"

    def __str__(self):
        return self.email


# почитать про прокси модель


class Teacher(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    LANGUAGE_CHOICES = {
        ('English', 'English'),
        ('German', 'German'),
        ('French', 'French'),
        ('Ukrainian', 'Ukrainian'),
        ('Polish', 'Polish'),
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    language = models.CharField("Teaching Language",choices=LANGUAGE_CHOICES, blank=True, max_length=15)
    hourly_rate = models.DecimalField("Hourly Rate", max_digits=5, decimal_places=2)
    status = models.CharField("Teacher Status", choices=STATUS_CHOICES, default='pending', max_length=10)
