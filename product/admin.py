from django.contrib import admin
from .models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['rates']
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = [
        "__str__",
        'slug',
        'price',
        'rates',
        'ia',
        'category'
    ]
    list_filter = [
        'ia',
        'price',
        'title'
    ]
    list_editable = [
        'ia'
    ]
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
