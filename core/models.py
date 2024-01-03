from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.managers import UserManager


# UserRoles = (
#     ("user", "user"),
#     ("manager", "manager"),
#     ("superadmin", "superadmin")
# )


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.IntegerField(unique=True, null=True)
    password = models.CharField(max_length=45)
    address = models.TextField(null=True)
    image = models.FileField(upload_to='images/', default="image.png")
    # role = models.CharField(max_length=50, choices=UserRoles, default="user")

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
