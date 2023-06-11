from django.contrib import admin
from .models import CallPrice

@admin.register(CallPrice)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product", "price", "category", "phone_number", "full_name", "status", "created_at"]
