# Generated by Django 3.2.4 on 2023-06-06 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0010_suggest'),
        ('Category', '0003_alter_category_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='قمیت')),
                ('phone_number', models.CharField(max_length=11, null=True, unique=True, verbose_name='شماره تماس')),
                ('full_name', models.CharField(max_length=100, null=True, verbose_name='نام و نام خانوادگی ')),
                ('compony_name', models.CharField(max_length=100, null=True, verbose_name='نام سازمان | شرکت')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت تایید')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Category.category', verbose_name='نوع دسته بندی')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.product', verbose_name='نام محصول')),
            ],
            options={
                'verbose_name': 'استعلام قیمت',
                'verbose_name_plural': 'استعلام قیمت ها',
            },
        ),
    ]
