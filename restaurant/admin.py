
from django.contrib import admin

from .models import RestaurantTable,RestaurantLocation

@admin.register(RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):

    list_display = (
        "table_number",
        "capacity",
        "qr_identifier",
        "is_active",
    )

    list_filter = ("is_active",)

    search_fields = ("table_number", "qr_code")

@admin.register(RestaurantLocation)
class RestaurantLocationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "latitude",
        "longitude",
        "geofence_radius",
        "is_active",
    )

    list_filter = ("is_active",)

    search_fields = ("name",)
