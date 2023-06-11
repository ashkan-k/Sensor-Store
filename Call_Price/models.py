from django.db import models
from Product.models import Product
from Category.models import Category

# Create your models here.
from utils.models import CustomModel


class CallPrice(CustomModel):
    product = models.ForeignKey(to=Product, blank=True, null=True, on_delete=models.CASCADE, related_name="products",verbose_name="نام محصول")
    category = models.ForeignKey(to=Category, blank=True, null=True, on_delete=models.CASCADE, related_name="categorys",verbose_name="نوع دسته بندی")
    price = models.IntegerField(verbose_name='قمیت')
    phone_number = models.CharField(
        max_length=11, unique=True, null=True, verbose_name="شماره تماس")
    full_name = models.CharField(
        max_length=100, null=True, verbose_name="نام و نام خانوادگی ")
    company_name = models.CharField(
        max_length=100, null=True, verbose_name="نام سازمان | شرکت")
    status = models.BooleanField(verbose_name='وضعیت تایید', default=False)

    def __str__(self):
        return f"{self.full_name} | {self.phone_number} | {self.product} | {self.created_at}"

    class Meta:
        verbose_name = "استعلام قیمت"
        verbose_name_plural = "استعلام قیمت ها"
