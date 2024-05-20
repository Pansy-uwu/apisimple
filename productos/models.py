from django.db import models

class Producto(models.Model):
    codigo_producto = models.CharField(max_length=20, unique=True, verbose_name="Código del producto")
    marca = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.codigo_producto})"

class Precio(models.Model):
    producto = models.ForeignKey(Producto, related_name='precios', on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.valor} ({self.fecha})"
