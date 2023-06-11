from django.db import models
from django.contrib.auth import get_user_model
from Product.models import Product, Color, Size
from utils.models import CustomModel


class Cart(CustomModel):
    user = models.ForeignKey(to=get_user_model(), related_name='carts', on_delete=models.CASCADE, verbose_name='کاربر')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='محصول')
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE, verbose_name='رنگ', null=True)
    size = models.ForeignKey(to=Size, on_delete=models.CASCADE, verbose_name='سایز', null=True)

    count = models.IntegerField(verbose_name='تعداد', default=1)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید'

    def get_total_price(self):
        return self.product.price * self.count

    def __str__(self):
        return self.user.full_name
