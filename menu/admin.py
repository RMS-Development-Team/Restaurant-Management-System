from django.contrib import admin

from .models import MenuCategory, MenuItem


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "category_id",
        "category_name",
        "description",
    )

    search_fields = ( "category_name")
    ordering = ("category_name",)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = (
        "item_id",
        "item_name",
        "category",
        "price",
        "availability",
    )

    list_filter = (
        "category",
        "availability"
    )

    search_fields = (
        "item_name",
        "category__category_name",
    )

    ordering = ("item_name",)

    list_editable = (
        "price",
        "availability",
    )

