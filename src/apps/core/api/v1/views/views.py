from src.apps.core.api.v1.serializers.serializers import ProductsSerializer,CategorySerializer
from src.apps.core.models import ProductsModel, CategoryModel
from rest_framework import viewsets


class ProductsView(viewsets.ModelViewSet):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer
    # filter_backends =


class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

