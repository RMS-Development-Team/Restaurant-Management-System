from django.db import models

from django.conf import settings
from django.utils import timezone


class KitchenTicket(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_PREPARING = 'Preparing'
    STATUS_READY = 'Ready'
    STATUS_CANCELLED = 'Cancelled'

    TICKET_STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_PREPARING, 'Preparing'),
        (STATUS_READY, 'Ready'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    ticket_id = models.AutoField(primary_key=True)
    
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='kitchen_tickets',
        db_column='order_id'
    )

    ticket_number = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    ticket_status = models.CharField(
        max_length=20,
        choices=TICKET_STATUS_CHOICES,
        default=STATUS_PENDING
    )

    created_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='created_by_user_id',
        related_name='created_kitchen_tickets'
    )

    class Meta:
        db_table = 'kitchen_tickets'
        ordering = ['-created_at']

    def __str__(self):
        return self.ticket_number
