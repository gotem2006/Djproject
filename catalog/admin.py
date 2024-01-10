from django.contrib import admin

# Register your models here.
from .models import Product, Category, ProductAttribute

admin.site.register([Product, Category, ProductAttribute])
