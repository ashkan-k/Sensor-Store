# Generated by Django 3.2.4 on 2023-06-14 16:09

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Coupon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='expiration',
            field=django_jalali.db.models.jDateTimeField(null=True, verbose_name='تاریخ انقضا'),
        ),
    ]