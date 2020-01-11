from django.contrib import admin
from pointofsale.models import Product, Category, PurchaseItem, Purchase


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)
