from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Номер телефона обязателен")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.username = email
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


class BaseUser(AbstractUser):
    """Base User model"""

    class UserRoleChoices(models.TextChoices):
        employer = "employer", "Работодатель"
        applicant = "applicant", "Работник"

    username = None
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    role = models.CharField(verbose_name="Роль", max_length=255, choices=UserRoleChoices.choices)
    name = models.CharField("Имя", max_length=50, blank=True, null=True)

    phone_number = models.CharField(verbose_name="Номер телефона", max_length=255, blank=True, null=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "role"]

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
