from django.urls import path
from . import views

app_name = "producto"

urlpatterns = [
    path("nuevo/", views.crearProducto, name="crear"),
    path("", views.listarProductos, name="lista"),
    path("<int:pk>/", views.detalleProducto, name="detalle"),
    path("<int:pk>/editar/", views.editarProducto, name="editar"),
    path("<int:pk>/borrar/", views.borrarProducto, name="borrar"),
]
