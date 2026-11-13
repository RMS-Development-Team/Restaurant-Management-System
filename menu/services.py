from django.db import transaction
from .models import MenuCategory, MenuItem


@transaction.atomic
def create_menu_category(validated_data):
    category = MenuCategory.objects.create(**validated_data)

    return category


@transaction.atomic
def update_menu_category(category, validated_data):

    for field, value in validated_data.items():
        setattr(category, field, value)

    category.save()
    return category


@transaction.atomic
def create_menu_item(validated_data):

    item = MenuItem.objects.create(**validated_data)

    return item

@transaction.atomic
def update_menu_item(item, validated_data):

    for field, value in validated_data.items():
        setattr(item, field, value)

    item.save()
    return item


@transaction.atomic
def update_menu_item_availability(item, availability):

    item.availability = availability
    item.save(update_fields=['availability'])

    return item