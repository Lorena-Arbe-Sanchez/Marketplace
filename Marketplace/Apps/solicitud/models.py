from django.db import models

from Apps.producto.models import Producto
from Apps.usuario.models import Usuario


class Solicitud(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('ACEPTADA', 'Aceptada'),
        ('CANCELADA', 'Cancelada'),
    ]

    codigo = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='PENDIENTE')
    mensaje = models.TextField(blank=True, null=True)

    # Relaciones
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario_interesado = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Solicitud de {self.usuario_interesado} por {self.producto}"