from django.contrib import admin
from src.apps.core.models import ProductsModel, CategoryModel

admin.site.register(ProductsModel)
admin.site.register(CategoryModel)
