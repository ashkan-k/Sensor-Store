# Generated by Django 3.2.4 on 2023-06-12 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Order', '0001_initial'),
        ('Product', '0011_alter_product_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Payment.payment', verbose_name='پرداخت'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='Product.product', verbose_name='محصول'),
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.size', verbose_name='سایز'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
