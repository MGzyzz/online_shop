from django.contrib import admin
from online_shop.models.product import Category, Product
from online_shop.models.item_in_cart import ItemInCart
from online_shop.models.order import Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category_id', 'remainder', 'price']
    list_filter = ['title', 'price']
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


class ItemCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity']
    list_filter = ['product']
    search_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'number_phone', 'address', 'date_and_creation', 'get_products']
    list_filter = ['number_phone', 'address']
    search_fields = ['number_phone']

    def get_products(self, obj):
        return ", ".join([str(product) for product in obj.products.all()])

    get_products.short_description = 'Products in Order'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ItemInCart, ItemCartAdmin)
admin.site.register(Order, OrderAdmin)
# Register your models here.
