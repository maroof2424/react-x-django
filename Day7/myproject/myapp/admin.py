from django.contrib import admin
from .models import Product

# admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('in_stock',)

admin.site.register(Product, ProductAdmin)
