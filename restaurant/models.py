import uuid
from django.db import models

class RestaurantTable(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveSmallIntegerField()
    qr_code = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number}"
