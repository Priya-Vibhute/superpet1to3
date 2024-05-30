from django.contrib import admin
from .models import Product,Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_description','category']

admin.site.register(Product,ProductAdmin)
# --------------------------------------------------------------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_slug']

# admin.site.register(Category,CategoryAdmin)

# admin.site.register(modelName)
# admin.site.register(modelName,modelAdmin)