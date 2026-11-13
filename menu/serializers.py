from rest_framework import serializers
from .models import MenuCategory, MenuItem

class MenuCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuCategory

        fields = [
            'category_id',
            'category_name',
            'description',
        ]

        read_only_fields = ['category_id']

    def validate_category_name(self, value):

        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Category name cannot be empty."
            )

        queryset = MenuCategory.objects.filter(
            category_name__iexact=value
        )

        if self.instance:
            queryset = queryset.exclude(
                category_id=self.instance.category_id
            )

        if queryset.exists():
            raise serializers.ValidationError(
                "This category already exists."
            )

        return value


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem

        fields = [
            'item_id',
            'category',
            'item_name',
            'description',
            'image',
            'price',
            'availability',
        ]

        read_only_fields = ['item_id']

    def validate_item_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Item name cannot be empty."
            )

        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero."
            )

        return value