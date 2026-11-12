from django.contrib import admin
from .models import KitchenTicket


@admin.register(KitchenTicket)
class KitchenTicketAdmin(admin.ModelAdmin):

    list_display = (
        "ticket_id",
        "ticket_number",
        "order",
        "ticket_status",
        "created_at",
        "created_by_user",
    )

    list_filter = (
        "ticket_status",
        "created_at",
    )

    search_fields = (
        "ticket_number",
        "order__id",
    )

    ordering = ("-created_at",)