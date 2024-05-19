"""Core models for our app."""

from autoslug import AutoSlugField

from django.contrib.auth.base_user import (
    BaseUserManager,
)
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from django.db import models

from versatileimagefield.fields import VersatileImageField

from common.models import BaseModelWithUID

from core.choices import (
    UserKind,
    UserGender,
)
from core.utils import get_user_media_path_prefix


class UserManager(BaseUserManager):
    """Managers for users."""

    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address.")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password):
        """Create a new superuser and return superuser"""

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.kind = UserKind.SUPER_ADMIN
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, BaseModelWithUID, PermissionsMixin):
    """Users in the System"""

    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        db_index=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        db_index=True,
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        db_index=True,
    )
    slug = AutoSlugField(
        populate_from="first_name",
        unique=True,
        db_index=True,
    )
    gender = models.CharField(
        max_length=20,
        blank=True,
        choices=UserGender.choices,
        default=UserGender.OTHER,
    )
    image = VersatileImageField(
        "Profile_image",
        upload_to=get_user_media_path_prefix,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    kind = models.CharField(
        max_length=20,
        choices=UserKind.choices,
        default=UserKind.UNDEFINED,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "first_name",
        "last_name",
    )

    class Meta:
        verbose_name = "System User"
        verbose_name_plural = "System Users"


class Profile(BaseModelWithUID):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_profile",
    )
    facebook_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )
    linkedin_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )
    instagram_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )
    designation = models.CharField(
        max_length=50,
        blank=True,
    )
    location = models.CharField(
        max_length=100,
        blank=True,
    )
    bio = models.TextField(
        blank=True,
    )
    address = models.TextField(
        blank=True,
    )

    def __str__(self) -> str:
        return f" {self.id} - {self.designation}"
