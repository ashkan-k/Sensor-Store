from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ["user" , "amount" , "status"]
    readonly_fields = [
        "created_at",
        "updated_at"
    ]