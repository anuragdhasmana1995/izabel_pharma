from django.contrib import admin
from . models import Products,  Medicine, Specification


class MedicineInline(admin.TabularInline):
    model = Medicine


class SpecificationInLine(admin.TabularInline):
    model = Specification


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_type',)
    inlines = [
        MedicineInline,
    ]


class MedicineAdmin(admin.ModelAdmin):
    list_display = ('med_name',)
    inlines = [
        SpecificationInLine,
    ]


admin.site.register(Products, ProductAdmin)
admin.site.register(Medicine, MedicineAdmin)







