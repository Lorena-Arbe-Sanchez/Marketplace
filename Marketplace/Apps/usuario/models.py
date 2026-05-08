from django.db import models


class Usuario(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.IntegerField() # TODO : ¿No debería ser string ya que no se hacen operaciones matemáticas con ello?

    def __str__(self):
        return self.nombre
