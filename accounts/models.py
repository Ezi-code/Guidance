from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
import uuid


class UserManager(BaseUserManager):
    use_in_migrations = True

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()

    def create(self, index_number, username, password, **kwargs: Any):
        if not index_number:
            raise ValueError("Index number field cannot be empty!")
        if not password:
            raise ValueError("Password field cannot be empty")
        user = self.model(index_number=index_number, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, index_number, username, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Usern must be staff")
        if extra_fields.get("is_active") is not True:
            raise ValueError("User must be active")
        return self.create_user(index_number, username, password, **extra_fields)

    def create_user(self, index_number, username, password, **extra_fields):
        if not index_number:
            raise ValueError("Index number field cannot be empty!")
        if not password:
            raise ValueError("Password field cannot be empty")
        user = self.model(index_number=index_number, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    table_name = "user"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    index_number = models.IntegerField(unique=True, db_index=True, default=None)
    username = models.CharField(max_length=100, default=None)
    phone = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "index_number"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} {self.index_number}"
