from django.contrib import admin
from .models import Product, Reseller, Item, Article, ServiceCenter


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'year', 'storage')
    search_fields = ['title', 'type', 'year', 'storage']
    date_hierarchy = 'created'


admin.site.register(Product, ProductAdmin)

admin.site.register([Reseller, ServiceCenter, Item, Article])
