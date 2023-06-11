from decouple import config
import json

from django.conf.urls.static import static
from zeep import Client
from django.db import models
import requests
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from django_jalali.db import models as jmodels
from ACL.permissions import PERMISSIONS
from utils.validator import mobile_regex, mobile_validator, national_id_regex
from .helpers import MARITAL_STATUS_CHOICES, EDUCATION_LEVEL_CHOICES, INTRO_METHOD
from .managers import UserManager
from django.conf import settings
from django.utils.text import slugify


# client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')

def upload_avatar(instance, filename):
    path = 'users/avatar/' + slugify(instance.phone, allow_unicode=True)
    return path + '/' + filename


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        null=True,
        blank=True,
        default="",
        max_length=100,
        verbose_name="نام",
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        default="",
        max_length=100,
        verbose_name="نام خانوادگی"
    )
    username = models.CharField('نام کاربری', max_length=50, unique=True)
    phone = models.CharField(verbose_name="شماره موبایل", max_length=11, unique=True, validators=[mobile_regex],
                             null=True, )
    date_joined = models.DateTimeField(verbose_name="تاریخ عضویت", default=timezone.now)
    last_login = models.DateTimeField(verbose_name="آخرین ورود", auto_now=True)
    is_superuser = models.BooleanField(verbose_name="آیا مدیر است؟", default=False)
    is_active = models.BooleanField(verbose_name="آیا فعال است؟", default=False)
    is_staff = models.BooleanField(verbose_name="آیا کارمند است؟", default=False)
    avatar = models.ImageField(verbose_name='عکس پروفایل', null=True, blank=True, upload_to=upload_avatar)

    address = models.TextField(
        null=True,
        blank=True,
        verbose_name='آدرس'
    )

    created_at = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )
    updated_at = jmodels.jDateTimeField(
        auto_now=True,
        verbose_name="تاریخ ویرایش"
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self.phone:
            self.phone = mobile_validator(
                str(self.phone)[: 11])

        if self.username:
            qs = User.objects.filter(
                username=self.username)
            if self.pk:
                qs = qs.exclude(id=self.pk)
            if qs.exists():
                raise ValidationError(
                    'نام کاربری تکراری است و برای کاربر دیگری استفاده شده است!', code="username")

        if self.phone:
            qs = User.objects.filter(
                phone=self.phone)
            if self.pk:
                qs = qs.exclude(id=self.pk)
            if qs.exists():
                raise ValidationError(
                    'شماره موبایل تکراری است و برای کاربر دیگری استفاده شده است!', code="mobile")

        return super().save(*args, **kwargs)

    def get_phone(self):
        return self.phone

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username or '---'

    def user_role(self):
        return self.role if hasattr(self, 'role') else None

    @property
    def role_code(self):
        if hasattr(self, 'role') and self.role.role:
            return self.role.role.code
        else:
            return None

    @property
    def role_code_display(self):
        return self.role.role_name if hasattr(self, 'role') else 'کاربر'

    @property
    def has_role(self):
        if hasattr(self, 'role'):
            return True
        return False

    def change_role(self, role):
        from ACL.models import UserRole
        user_role, _ = UserRole.objects.get_or_create(user=self)
        user_role.role = role
        user_role.save()
        return True

    @property
    def permissions(self):
        if self.is_superuser:
            return PERMISSIONS
        else:
            try:
                return self.role.role.permissions_list
            except:
                return []

    def check_has_permission(self, permission):
        if permission in self.permissions:
            return True
        return False

    def get_avatar(self):
        return self.avatar.url if self.avatar else '/static/admin_panel/assets/img/user_avatr.png'

    @property
    def get_education_level(self):
        return dict(EDUCATION_LEVEL_CHOICES).get(self.education_level, '')

    @property
    def get_intro_method(self):
        return dict(INTRO_METHOD.CHOICES).get(self.intro_method, '---')