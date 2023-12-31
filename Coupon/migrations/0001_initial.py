# Generated by Django 3.2.4 on 2023-06-07 12:29

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('code', models.CharField(max_length=250, verbose_name='کد')),
                ('percent', models.IntegerField(verbose_name='درصد تخفیف')),
                ('uses_number', models.IntegerField(default=1, verbose_name='تعداد قابل استفاده')),
                ('expiration', models.CharField(max_length=50, verbose_name='تاریخ انقضا')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کد تخفیف ها',
            },
        ),
    ]
