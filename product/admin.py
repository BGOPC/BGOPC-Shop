from django.contrib import admin
from .models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','ia','is_deleted']
    list_filter = ['price','ia','is_deleted']
    list_editable = ['price','ia','is_deleted']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)