from django.contrib import admin
from carts.models import Cart

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = [ 'product', 'quantity', 'created_timestap', ]
    search_fields = ('product', 'quantity', 'created_timestap', )
    readonly_fields = ('created_timestap',)
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_timestap', ]
    list_filter = ['user', 'product',  'created_timestap', ]


