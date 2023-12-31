# Generated by Django 3.2.4 on 2023-06-12 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Coupon', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=255, null=True, verbose_name='مبلغ')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('authority', models.CharField(max_length=255, null=True, verbose_name='کد بازگشتی درگاه')),
                ('ref_code', models.CharField(max_length=255, null=True, verbose_name='شناسه پیگیری')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ خرید')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('coupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coupon.coupon', verbose_name='کد تخفیف')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربری')),
            ],
            options={
                'verbose_name': 'پرداخت',
                'verbose_name_plural': 'پرداخت ها',
            },
        ),
    ]
