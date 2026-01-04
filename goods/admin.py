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
    list_display = ('name', 'slug', 'description', 'price', 'discount', 'quantity')
    search_fields = ('name',)
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}