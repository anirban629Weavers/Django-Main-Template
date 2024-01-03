from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_args):
        if not email:
            raise ValueError("Email cannot be empty")
        else:
            try:
                validate_email(email)
            except Exception:
                raise ValidationError("Enter a valid email address")

        user = self.model(
            email=self.normalize_email(email),
            **extra_args
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_args):
        user = self.create_user(
            email=email,
            password=password,
            **extra_args
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
