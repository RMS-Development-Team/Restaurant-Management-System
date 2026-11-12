
from django.conf import settings
from django.db import models


class Order(models.Model):

    class OrderType(models.TextChoices):
        QR = "QR", "QR"
        WAITER = "WAITER", "Waiter"
        COUNTER = "COUNTER", "Counter"

    class OrderStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        PREPARING = "PREPARING", "Preparing"
        READY = "READY", "Ready"
        HANDED_OVER = "HANDED_OVER", "Handed Over"
        SERVED = "SERVED", "Served"
        CANCELLED = "CANCELLED", "Cancelled"

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="customer_orders",
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_orders",
        null=True,
        blank=True
    )

    table = models.ForeignKey(
        "restaurant.RestaurantTable",
        on_delete=models.PROTECT,
        related_name="orders",
        null=True,
        blank=True
    )

    order_type = models.CharField(
        max_length=20,
        choices=OrderType.choices
    )

    token_number = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    menu_item = models.ForeignKey(
        "menu.MenuItem",
        on_delete=models.PROTECT,
        related_name="order_items"
    )

    quantity = models.PositiveIntegerField(default=1)

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.item_name} x {self.quantity}"

    @property
    def subtotal(self):
        return self.quantity * self.unit_price


class OrderStatusHistory(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="status_history"
    )

    old_status = models.CharField(
        max_length=20,
        choices=Order.OrderStatus.choices,
        blank=True
    )

    new_status = models.CharField(
        max_length=20,
        choices=Order.OrderStatus.choices
    )

    changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="order_status_changes",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Order #{self.order_id}: "
            f"{self.old_status} -> {self.new_status}"
        )
