from django.contrib import admin
from apps.product.models import Product, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['status', 'title_product', 'category', 'price', 'user', 'time_create']
    list_filter = ['status', 'time_create', 'category']
    # list_editable = ['is_active']
    list_display_links = ("title_product",)
    search_fields = ("title", 'description', 'category', 'address', 'status')
    ordering = ("-time_create",)




# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['text', 'user', 'product', 'time_create']

admin.site.register(ProductImage)