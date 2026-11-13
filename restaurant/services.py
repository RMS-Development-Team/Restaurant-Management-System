
import uuid
import math

from django.db import transaction
from .models import RestaurantTable, RestaurantLocation


def generate_qr_identifier():
    return uuid.uuid4().hex


@transaction.atomic
def create_restaurant_table(validated_data):

    validated_data["qr_identifier"] = generate_qr_identifier()

    return RestaurantTable.objects.create(**validated_data)



def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two GPS coordinates in meters.
    """

    earth_radius = 6371000  # meters

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius * c


def validate_geofence(location, user_latitude, user_longitude):

    if not location.is_active:
        return False

    distance = calculate_distance(
        location.latitude,
        location.longitude,
        user_latitude,
        user_longitude
    )

    return distance <= location.geofence_radius
