#
from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser, Group  # ここを追加
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="customuser_groups",  # ここを変更
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="customuser_permissions",  # ここを変更
        related_query_name="customuser",
    )
