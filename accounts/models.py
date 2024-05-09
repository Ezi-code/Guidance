from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
import uuid

# Create your models here.


class UserManager(BaseUserManager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()

    def create_user(self, username, password, **kwargs: Any) -> Any:
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user
        # return super().create(username, password, **kwargs)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Usern must be staff")
        if extra_fields.get("is_active") is not True:
            raise ValueError("User must be active")
        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, null=False, blank=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
