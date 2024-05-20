from rest_framework import serializers
from .models import Producto, Precio

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','codigo_producto','marca','codigo','nombre')

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = ('id', 'producto', 'fecha', 'valor')
        read_only_fields = ('fecha', )