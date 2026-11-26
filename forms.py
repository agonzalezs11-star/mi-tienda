from django import forms
from .models import Cliente, Proveedor, Marca, Categoria, Producto, Compra, Venta
class EstiloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs["class"] = "campo"
class ClienteForm(EstiloForm):
    class Meta: model=Cliente; fields="__all__"
class ProveedorForm(EstiloForm):
    class Meta: model=Proveedor; fields="__all__"
class MarcaForm(EstiloForm):
    class Meta: model=Marca; fields="__all__"
class CategoriaForm(EstiloForm):
    class Meta: model=Categoria; fields="__all__"
class ProductoForm(EstiloForm):
    class Meta: model=Producto; fields="__all__"
class CompraForm(EstiloForm):
    class Meta: model=Compra; fields=["proveedor","observacion"]
class VentaForm(EstiloForm):
    class Meta: model=Venta; fields=["cliente","forma_pago"]
