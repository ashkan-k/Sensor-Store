# Generated by Django 4.0.4 on 2022-05-16 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ACL', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='ACL.role', verbose_name='نقش')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='role', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نقش کاربر',
                'verbose_name_plural': 'نقش کاربران',
            },
        ),
    ]
