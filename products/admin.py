from django.contrib import admin

from products.models import Product, category

# Register your models here.
admin.site.register(Product)
admin.site.register(category)