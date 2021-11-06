from django.contrib import admin
from django.contrib import admin as auth_admin

from .models import Shop, ShopReading


@admin.register(Shop)
class ShopAdmin(auth_admin.ModelAdmin):
    list_display = ["id", "uuid", "name"]
    search_fields = ["name"]


@admin.register(ShopReading)
class ShopReadingAdmin(auth_admin.ModelAdmin):
    list_display = ["gtin", "get_shop", "expiry_date", "reading_time"]
    search_fields = ["gtin"]

    def get_shop(self, obj):
        return obj.shop.name
