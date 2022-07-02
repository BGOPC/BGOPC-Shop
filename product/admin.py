from django.contrib import admin
from . import models


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
        'ia'
    ]
    list_filter = [
        'ia',
        'price',
        'title'
    ]
    list_editable = [
        'ia'
    ]
admin.site.register(models.Product, ProductAdmin)
