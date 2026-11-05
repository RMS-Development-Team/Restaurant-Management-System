from django.contrib import admin
from .models import User, OTPVerification
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "mobile_number",
        "email",
        "role",
        "is_active",
        "is_staff",
    )

    search_fields = ("name", "mobile_number", "email")
    list_filter = ("role", "is_active", "is_staff")


@admin.register(OTPVerification)
class OTPVerificationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "is_verified",
        "attempts",
        "created_at",
        "expires_at",
    )

    list_filter = ("is_verified", "created_at")
    readonly_fields = ("created_at",)
