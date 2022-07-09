from django.contrib import admin
from .models import Product, Reseller, Item, Article, ServiceCenter

# Register your models here.

admin.site.register([Product, Reseller, ServiceCenter, Item, Article])
