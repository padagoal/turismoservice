from django.db import models
from TurismoPlace.models import Lugar
from django.contrib.auth.models import User

# Create your models here.


class Tour(models.Model):
    tour_name = models.CharField(max_length=255,verbose_name="Nombre Itinerario")
    tour_short_descripcion = models.CharField(max_length=255,verbose_name="Descripcion Corta de Itinerario")
    tour_description = models.TextField(max_length=5000,verbose_name="Descripcion Itinerario")
    tour_description_aditional = models.TextField(max_length=5000,verbose_name="Descripcion Itinerario")
    tour_photo_cover = models.ImageField(upload_to='itinerario/', null=True)
    tour_lugar = models.ManyToManyField(Lugar,related_name="tour_places")
    tour_cost = models.IntegerField(default=0,verbose_name="Costo Itinerario")
    is_from_user = models.BooleanField(default=False,verbose_name="Es de un Usuario?")
    is_from_staff = models.BooleanField(default=True,verbose_name="Es del Staff?")
    tour_hour_begin = models.TimeField(verbose_name="Hora Inicio del Itinerario",null=True)
    tour_hour_end = models.TimeField(verbose_name="Hora Fin del Itinerario",null=True)
    tour_active = models.BooleanField(default=True,verbose_name="Activo")

    user_id = models.IntegerField(default=0,verbose_name="user_id",null=True,blank=True)

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Itinerario"
        verbose_name_plural = "Itinerarios"

    def get_places_names(self):
        return " - ".join([p.name_place for p in self.tour_lugar.all()])

    def get_ciudades(self):
        return " - ".join([p.ciudad_lugar.nombre_ciudad for p in self.tour_lugar.all()])

    def get_ciudades_salto(self):
        return " \n ".join([p.ciudad_lugar.nombre_ciudad for p in self.tour_lugar.all()])

    def __str__(self):
        return self.tour_name


class TourReserva(models.Model):
    user_id = models.IntegerField(verbose_name='User Id',default=0)
    tour_selected = models.ForeignKey(Tour,related_name='tour_selected_by_user',on_delete=models.DO_NOTHING)
    fecha_tour_reserva = models.DateField(verbose_name='Fecha Reserva')
    tour_cost = models.IntegerField(default=0,verbose_name='Costo Itinerario')
    cantidad_personas_tour = models.IntegerField(default=1,verbose_name='Cantidad de Personas en el Tour')
    active = models.BooleanField(default=True)
    concretado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Reserva de Tour'
        verbose_name_plural = 'Reservas de Tours'

    def __str__(self):
        return f'User (PK: {self.user_id}, Tour: {self.tour_selected.tour_name})'