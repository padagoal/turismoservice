from django.db import models
from TurismoPlace.models import Ciudad
# Create your models here.


class Bus(models.Model):
    ciudad_partida = models.IntegerField(default=0,verbose_name='ciudad_partida_bus')
    ruta = models.IntegerField(default=0,verbose_name='Ruta')
    ciudad_partida_desc = models.TextField(max_length=100,verbose_name='Descripcion Partida')
    ciudad_destino = models.IntegerField(default=0,verbose_name='ciudad_destino_bus')
    ciudad_destino_desc = models.TextField(max_length=100, verbose_name='Descripcion Destino')
    precio = models.IntegerField(default=0,verbose_name='Precio')

    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'

    def __str__(self):
        return f'Bus (PK: {self.pk}, CiudadPartida: {self.ciudad_partida}), ' \
               f'CiudadDestino: {self.ciudad_destino})'


class BusDto(models.Model):
    ciudad_partida = models.ForeignKey(Ciudad, related_name='ciudad_partida_bus',on_delete=models.SET_NULL,null=True)
    ruta = models.IntegerField(default=0, verbose_name='Ruta')
    ciudad_partida_desc = models.TextField(max_length=100, verbose_name='Descripcion Partida')
    ciudad_destino = models.ForeignKey(Ciudad, related_name='ciudad_destino_bus',on_delete=models.SET_NULL,null=True)
    ciudad_destino_desc = models.TextField(max_length=100, verbose_name='Descripcion Destino')
    precio = models.IntegerField(default=0, verbose_name='Precio')

    class Meta:
        verbose_name = 'BusDto'
        verbose_name_plural = 'BusesDto'

    def __str__(self):
        return f'Bus (PK: {self.pk}, CiudadPartida: {self.ciudad_partida}), ' \
               f'CiudadPartida: {self.ciudad_destino})'
