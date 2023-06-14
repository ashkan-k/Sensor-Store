from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels
from utils.models import CustomModel


class Coupon(CustomModel):
    code = models.CharField(verbose_name='کد', max_length=250)
    percent = models.IntegerField(verbose_name='درصد تخفیف')
    uses_number = models.IntegerField(verbose_name='تعداد قابل استفاده', default=1)
    expiration = jmodels.jDateField(
        null=True,
        verbose_name="تاریخ انقضا"
    )

    # user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, verbose_name='کاربر', null=True, blank=True)

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد تخفیف ها'

    def __str__(self):
        return f"dfds"
