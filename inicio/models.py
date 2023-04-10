from django.db import models

# Create your models here.


class Carro(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    año_fabricacion = models.IntegerField()
    
    def __str__(self):
        return f'El carro {self.modelo} de la marca {self.marca} tiene el precio de {self.precio} y su fabricación es del año {self.año_fabricacion}'