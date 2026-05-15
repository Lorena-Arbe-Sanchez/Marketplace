from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


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
    # 1. Obtener parámetros de la URL (?categoria=...&estado=...)
    cat_id = request.GET.get('categoria')
    estado = request.GET.get('estado')

    # 2. Empezar con todos los productos
    productos = Producto.objects.all()

    # 3. Aplicar filtros si existen
    if cat_id:
        productos = productos.filter(categoria_id=cat_id)
    if estado:
        productos = productos.filter(estado=estado)

    # 4. Pasar también las categorías para el desplegable
    from .models import Categoria
    categorias = Categoria.objects.all()

    return render(request, "producto/producto.html", {
        "productos": productos,
        "categorias": categorias
    })


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
