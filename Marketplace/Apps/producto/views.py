from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


# Create your views here.

def crearProducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:lista")
    else:
        form = ProductoForm()

    return render(
        request,
        "producto/producto_form.html",
        {"form": form, "modo": "crear"}

    )


def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, "producto/producto.html", {"productos": productos})


def detalleProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "producto/producto_detail.html", {"producto": producto})


def editarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("producto:detalle", pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)

    return render(
        request,
        "producto/producto_form.html",
        {
            "form": form,
            "modo": "editar",
            "producto": producto
        }
    )


def borrarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        producto.delete()
        return redirect("producto:lista")

    return render(
        request,
        "producto/producto_confirm_delete.html",
        {"producto": producto}
    )
