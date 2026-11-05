
from django.contrib import admin

from .models import RestaurantTable

@admin.register(RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):

    list_display = (
        "table_number",
        "capacity",
        "qr_code",
        "is_active",
    )

    list_filter = ("is_active",)

    search_fields = ("table_number", "qr_code")
