from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug', )
    list_display = ('sku', 'name', 'sku', 'date_created')
    list_display_links = ('sku', 'name')
    search_fields = ('name', 'sku' )
    list_per_page = 25

admin.site.register(Product, ProductAdmin)
