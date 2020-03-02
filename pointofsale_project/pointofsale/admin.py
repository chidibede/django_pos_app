from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from pointofsale.models import Product, Category, PurchaseItem, Purchase


# Register your models here.

class ProductAdmin(ImportExportModelAdmin):
    pass

class CategoryAdmin(ImportExportModelAdmin):
    pass

class PurchaseAdmin(ImportExportModelAdmin):
    pass

class PurchaseItemAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem, PurchaseItemAdmin)
# @admin.register(Category)
# @admin.register(Product)
# @admin.register(Purchase)
# @admin.register(PurchaseItem)


