from django.db import models

from Apps.usuario.models import Usuario


class Categoria(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    # Definir los estados posibles
    ESTADOS = [
        ('DISPONIBLE', 'Disponible'),
        ('RESERVADO', 'Reservado'),
        ('VENDIDO', 'Vendido'),
    ]

    codigo = models.IntegerField(unique=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    estado = models.CharField(
        max_length=15,
        choices=ESTADOS,
        default='DISPONIBLE'
    )

    # La fecha actual se pondrá automáticamente al crear el objeto
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    # La categoría del producto
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    # El usuario que lo vende
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.titulo
