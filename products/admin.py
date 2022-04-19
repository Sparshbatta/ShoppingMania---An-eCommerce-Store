from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug_title']
    prepopulated_fields = {'slug_title':('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','price','in_stock',
    'created_at','updated_at']
    list_filter = ['in_stock','is_active']
    list_editable = ['price','in_stock']
    prepopulated_fields = {'slug':('title',)}
