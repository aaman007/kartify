from django.contrib import admin

from kartify.store.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'is_available']
    prepopulated_fields = {'slug': ['name']}
