# Generated by Django 3.2.4 on 2023-06-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0012_auto_20230613_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='short_text',
        ),
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, null=True, related_query_name='product', to='Product.Color', verbose_name='رنگ ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(blank=True, null=True, related_query_name='product', to='Product.Size', verbose_name='سایز ها'),
        ),
    ]
