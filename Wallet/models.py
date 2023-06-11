from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Wallet(models.Model):
    user = models.OneToOneField(verbose_name='کاربر' , to=User , on_delete=models.CASCADE , related_name='wallet')
    amount = models.PositiveBigIntegerField(verbose_name='مبلغ')
    status = models.BooleanField(verbose_name='وضعیت' , default=True)

    created_at = models.DateTimeField(verbose_name='تاریخ ثبت' , auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='تاریخ ویرایش' , auto_now=True)

    class Meta:
        verbose_name = 'کیف پول'
        verbose_name_plural = 'کیف پول ها'

    def __str__(self):
        return self.user.username