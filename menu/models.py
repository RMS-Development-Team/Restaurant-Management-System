from django.db import models


from django.db import models


# 1. Menu Categories Table
class MenuCategory(models.Model):

    category_id = models.AutoField(primary_key=True)

    category_name = models.CharField(max_length=100)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'menu_categories'
        verbose_name = 'Menu Category'
        verbose_name_plural = 'Menu Categories'


# 2. Menu Items Table
class MenuItem(models.Model):

    item_id = models.AutoField(primary_key=True)

    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        db_column='category_id',
        related_name='items'
    )

    item_name = models.CharField(max_length=100)

    description = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name

    class Meta:
        db_table = 'menu_items'
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
