from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category_id', 'remainder', 'price']
    list_filter = ['title', 'price']
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
