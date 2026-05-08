from django.db import models

from Apps.usuario.models import Usuario


class Categoria(models.Model):
    codigo = models.IntegerField()  # TODO : Poner autoincremental? (Para que cada vez que se inserte uno, se le ponga un código único como ID)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


# Create your models here.
class Producto(models.Model):
    codigo = models.IntegerField()  # TODO : Poner autoincremental? (Para que cada vez que se inserte uno, se le ponga un código único como ID)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)  # TODO : Ya revisaremos si cambiar el tipo de dato
    fecha_publicacion = models.DateTimeField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo
