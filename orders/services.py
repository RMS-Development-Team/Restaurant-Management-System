
from django.db import transaction
from .models import Order, OrderStatusHistory


@transaction.atomic
def update_order_status(order, new_status, changed_by=None):

    old_status = order.status

    if old_status == new_status:
        return order

    order.status = new_status
    order.save(update_fields=["status", "updated_at"])

    OrderStatusHistory.objects.create(
        order=order,
        old_status=old_status,
        new_status=new_status,
        changed_by=changed_by
    )

    return order
