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
    tour_hour_begin = models.TimeField(verbose_name="Hora Inicio del Itinerario")
    tour_hour_end = models.TimeField(verbose_name="Hora Fin del Itinerario")
    tour_active = models.BooleanField(default=True,verbose_name="Activo")

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Itinerario"
        verbose_name_plural = "Itinerarios"

    def __str__(self):
        return self.tour_name


class TourByUser(models.Model):
    tour_fk = models.ManyToOneRel(Tour,on_delete=models.CASCADE,field_name='tour_user_fk',to=Tour)
    user_tour = models.OneToOneField(User, on_delete=models.CASCADE)
    active_tour_user = models.BooleanField(verbose_name='Esta Activo?',default=True)

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Itinerario por Usuario"
        verbose_name_plural = "Itinerarios por Usuarios"
