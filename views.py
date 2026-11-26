from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Sum
from . import models, forms

@login_required
def inicio(request):
    return render(request, "tienda/inicio.html", {
        "clientes": models.Cliente.objects.count(),
        "productos": models.Producto.objects.count(),
        "proveedores": models.Proveedor.objects.count(),
        "ventas": models.Venta.objects.count(),
        "compras": models.Compra.objects.count(),
        "stock_bajo": models.Producto.objects.filter(stock__lte=5).count(),
    })

@login_required
def listado(request, modelo, formulario, titulo):
    registros = modelo.objects.all().order_by("-id")
    return render(request, "tienda/listado.html", {"registros":registros,"titulo":titulo})

@login_required
def guardar(request, modelo, formulario, titulo, pk=None):
    instancia = get_object_or_404(modelo, pk=pk) if pk else None
    form = formulario(request.POST or None, instance=instancia)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"{titulo} guardado correctamente.")
        return redirect("lista_"+modelo.__name__.lower())
    return render(request, "tienda/formulario.html", {"form":form,"titulo":titulo})

@login_required
def eliminar(request, modelo, titulo, pk):
    obj=get_object_or_404(modelo,pk=pk)
    if request.method=="POST":
        obj.delete()
        messages.success(request, f"{titulo} eliminado.")
        return redirect("lista_"+modelo.__name__.lower())
    return render(request,"tienda/confirmar.html",{"obj":obj,"titulo":titulo})

def construir_vistas(modelo, formulario, titulo):
    def lista(request): return listado(request, modelo, formulario, titulo)
    def nuevo(request): return guardar(request, modelo, formulario, titulo)
    def editar(request, pk): return guardar(request, modelo, formulario, titulo, pk)
    def borrar(request, pk): return eliminar(request, modelo, titulo, pk)
    return lista,nuevo,editar,borrar
