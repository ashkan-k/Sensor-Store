from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from ACL.models import Role
from utils.models import CustomModel
from utils.validator import validate_file_size, mobile_regex

User = get_user_model()


class Suggestion(CustomModel):
    user = models.ForeignKey(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='suggestions')
    title = models.CharField(verbose_name='عنوان', max_length=255)
    text = models.TextField(verbose_name='متن توضیحات')

    class Meta:
        verbose_name = 'انتقادات و پیشنهادات'
        verbose_name_plural = 'انتقادات و پیشنهادات'

    def __str__(self):
        return f"{self.user}-{self.title}" or '---'


class ContactUs(CustomModel):
    first_name = models.CharField(verbose_name='نام', max_length=255)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=255)
    phone = models.CharField(verbose_name="شماره موبایل", max_length=11, validators=[mobile_regex])
    email = models.EmailField(verbose_name='ایمیل')
    title = models.CharField(verbose_name='عنوان', max_length=255)
    text = models.TextField(verbose_name='متن توضیحات')

    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباط با ما'

    def __str__(self):
        return f"{self.first_name}-{self.last_name}" or '---'
