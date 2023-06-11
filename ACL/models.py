from django.db import models
from utils.models import CustomModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Role(CustomModel):
    name = models.CharField(max_length=50, verbose_name='نام نمایشی')
    code = models.CharField(verbose_name='عنوان انگلیسی', max_length=255, unique=True)
    description = models.TextField(max_length=500, verbose_name='توضیحات', null=True, blank=True)
    permissions = models.ManyToManyField(to='Permission', related_name='role', verbose_name='نقش ها', blank=True)

    class Meta:
        verbose_name = 'نقش'
        verbose_name_plural = 'نقش ها'

    def __str__(self):
        return f"{self.name}"

    @property
    def permissions_list(self):
        return list(self.permissions.values_list('code', flat=True))


class Permission(CustomModel):
    name = models.CharField(max_length=50, verbose_name='نام نمایشی')
    code = models.CharField(verbose_name='عنوان انگلیسی', max_length=255, unique=True)
    description = models.TextField(max_length=500, verbose_name='توضیحات', null=True, blank=True)

    class Meta:
        verbose_name = 'دسترسی'
        verbose_name_plural = 'دسترسی ها'

    def __str__(self):
        return f"{self.name}-{self.code}"


class UserRole(CustomModel):
    role = models.ForeignKey(to=Role, on_delete=models.CASCADE, related_name='users', verbose_name='نقش', null=True, blank=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='role', verbose_name='کاربر')

    class Meta:
        verbose_name = 'نقش کاربر'
        verbose_name_plural = 'نقش کاربران'

    def __str__(self):
        return f"{self.user}-{self.role.name}"

    @property
    def role_name(self):
        if self.role:
            return self.role.name
        return 'کاربر'
