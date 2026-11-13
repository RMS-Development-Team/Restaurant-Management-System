import uuid
from django.db import models

class RestaurantTable(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveSmallIntegerField()
    qr_identifier = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number}"


class RestaurantLocation(models.Model):

    name = models.CharField(max_length=150)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )

    geofence_radius = models.PositiveIntegerField(
        default=150
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

