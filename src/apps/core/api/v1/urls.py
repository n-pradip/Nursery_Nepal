from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.apps.core.api.v1.views import views


router = DefaultRouter()
router.register('product', views.ProductsView, basename='all_products'),
router.register('category', views.CategoryView, basename='Categories'),

# urlpatterns = [
#     path('product', views.ProductsView, name='all_products'),
#     path('category', views.CategoryView, name='Categories'),
#     path("^", include(router.urls))
# ]

urlpatterns = router.urls
