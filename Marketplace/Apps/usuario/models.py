from django.db import models


class Usuario(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(
        max_length=100)  # Poner 2 apellidos para diferenciar los datos en caso de por ejemplo tener que editar solo uno de ellos
    apellido2 = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=9)  # Establecer el teléfono sin prefijo, solo los 9 números

    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}"
