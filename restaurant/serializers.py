
from rest_framework import serializers
from .models import RestaurantTable, RestaurantLocation
from .services import create_restaurant_table


class RestaurantTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantTable
        fields = [
            "id",
            "table_number",
            "capacity",
            "qr_identifier",
            "is_active",
        ]
        read_only_fields = ["id", "qr_identifier"]

    def validate_table_number(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Table number must be greater than zero."
            )
        return value

    def validate_capacity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Table capacity must be greater than zero."
            )
        return value

def create(self, validated_data):
    return create_restaurant_table(validated_data)




class RestaurantLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantLocation
        fields = [
            "id",
            "name",
            "latitude",
            "longitude",
            "geofence_radius",
            "is_active",
        ]
        read_only_fields = ["id"]

    def validate_latitude(self, value):
        if not -90 <= value <= 90:
            raise serializers.ValidationError(
                "Latitude must be between -90 and 90."
            )
        return value

    def validate_longitude(self, value):
        if not -180 <= value <= 180:
            raise serializers.ValidationError(
                "Longitude must be between -180 and 180."
            )
        return value

    def validate_geofence_radius(self, value):
        if not 100 <= value <= 200:
            raise serializers.ValidationError(
                "Geofence radius must be between 100 and 200 meters."
            )
        return value
