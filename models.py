from django.db import models
from django.core.validators import MinValueValidator

class Marca(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    origen = models.CharField(max_length=60, blank=True)
    def __str__(self): return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField(blank=True)
    def __str__(self): return self.nombre

class Cliente(models.Model):
    identificacion = models.CharField(max_length=13, unique=True)
    nombres = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    def __str__(self): return f"{self.nombres} ({self.identificacion})"

class Proveedor(models.Model):
    identificacion = models.CharField(max_length=13, unique=True)
    empresa = models.CharField(max_length=120)
    contacto = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    def __str__(self): return self.empresa

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    codigo = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField(blank=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categorias = models.ManyToManyField(Categoria, blank=True)
    activo = models.BooleanField(default=True)
    def __str__(self): return f"{self.codigo} - {self.nombre}"

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    observacion = models.TextField(blank=True)
    def __str__(self): return f"Compra #{self.pk}"

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name="detalles", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    def __str__(self): return f"{self.producto} x {self.cantidad}"

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    forma_pago = models.CharField(max_length=30, default="Efectivo")
    def __str__(self): return f"Venta #{self.pk}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name="detalles", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    def __str__(self): return f"{self.producto} x {self.cantidad}"
