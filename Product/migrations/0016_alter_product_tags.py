# Generated by Django 3.2.4 on 2023-06-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0015_auto_20230613_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.CharField(blank=True, help_text='تگ ها را با ویرگول از هم جداکنید.', max_length=250, null=True, verbose_name='تگ ها'),
        ),
    ]