from .models import Producto, Precio
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer, PrecioSerializer  # Corrección en la ruta de importación

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class PrecioViewSet(viewsets.ModelViewSet):
    queryset = Precio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PrecioSerializer