from django.contrib import admin
from .models import *
class DetalleCompraInline(admin.TabularInline):
    model=DetalleCompra
    extra=1
class DetalleVentaInline(admin.TabularInline):
    model=DetalleVenta
    extra=1
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display=("id","proveedor","fecha","total")
    inlines=[DetalleCompraInline]
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display=("id","cliente","fecha","total")
    inlines=[DetalleVentaInline]
admin.site.register([Cliente,Proveedor,Marca,Categoria,Producto])
