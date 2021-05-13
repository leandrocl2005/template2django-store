from .models import Category, Product
from django.contrib import admin


# Register your models here.
class ProductAdmin(admin.ModelAdmin):

  list_display = ('name', 'category', 'recommended', "popular", 'created_at')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
