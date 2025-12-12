from django.contrib import admin
from .models import Product, Reseller, Item, Article, ServiceCenter


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'year', 'storage')
    search_fields = ['title', 'type', 'year', 'storage']
    date_hierarchy = 'created'

admin.site.register(Product, ProductAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'reseller', 'price', 'active')
    search_fields = ['product__title', 'reseller__name', 'price']

admin.site.register(Item, ItemAdmin)

admin.site.register([Reseller, ServiceCenter, Article])
