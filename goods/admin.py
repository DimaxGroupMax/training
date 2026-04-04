from django.contrib import admin
from .models import Categories, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}




@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'discount', 'quantity')
    search_fields = ('name', 'description')
    list_filter = ('category',  'discount', 'quantity')
    list_editable = ['discount',]
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name',
        'category',
        'slug',
        'description',
        ('price', 'discount'),
        'quantity'
    ]