
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer",
        "table",
        "order_type",
        "status",
        "created_at",
    )

    list_filter = (
        "order_type",
        "status",
    )

    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "order",
        "menu_item",
        "quantity",
        "unit_price",
    )
