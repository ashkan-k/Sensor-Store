# Generated by Django 3.2.4 on 2023-06-13 13:45

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0011_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=500, verbose_name='قمیت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.CharField(help_text='تگ ها را با ویرگول از هم جداکنید.', max_length=250, verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش'),
        ),
    ]
