from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product Management APIs
    -----------------------
    GET  /api/admin/products/
    POST /api/admin/products/
    PUT  /api/admin/products/{id}/
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
