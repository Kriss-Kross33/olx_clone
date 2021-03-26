from django.contrib import admin
from .models import Product, Category, Brand, ProductImages
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['created', 'owner']


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['category_name']

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImages)