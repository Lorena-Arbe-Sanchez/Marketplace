from django.contrib import admin

# Register your models here.
from .models import Producto, Categoria

admin.site.register(Producto)

# Aquí se registra el modelo Categoria para que sea visible en el panel de administración de Django.
admin.site.register(Categoria)