from django.db import models
from TurismoPlace.models import Lugar
# Create your models here.

class ServiceHotel(models.Model):
    service_name = models.CharField(verbose_name='Servicios del Hotel',max_length=100)
    service_icon = models.ImageField(upload_to='hotel/icon', null=True, blank=True)

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Servicio de Hotel'
        verbose_name_plural = 'Servicios de Hotel'

    def __str__(self):
        return self.service_name


class ServiceRoom(models.Model):
    service_name = models.CharField(verbose_name='Servicios de la Habitacion',max_length=100)
    service_icon = models.ImageField(upload_to='room/icon', null=True, blank=True)

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Servicio de la Habitacion'
        verbose_name_plural = 'Servicios de la Habitacion'

    def __str__(self):
        return self.service_name


class Hotel(models.Model):
    hotel_lugar = models.ForeignKey(Lugar,limit_choices_to={'is_hotel':True},on_delete=models.DO_NOTHING)
    hotel_stars = models.IntegerField(default=1)
    hotel_services = models.ManyToManyField(ServiceHotel,related_name='service_name_hotel')

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True,blank=True)

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'

    def __str__(self):
        return self.hotel_lugar.name_place

    def get_hotel_services(self):
        return "\n".join([p.service_name for p in self.hotel_services.all()])


class Rooms(models.Model):
    room_hotel = models.ForeignKey(Hotel,on_delete=models.DO_NOTHING)
    room_name = models.CharField(max_length=100,verbose_name='Nombre Habitacion')
    room_desc = models.TextField(max_length=2000,verbose_name='Descripcion Habitacion')
    room_capacity_adult = models.IntegerField(default=1,verbose_name='Capacidad de Habitacion para Adultos')
    room_capacity_child = models.IntegerField(default=0, verbose_name='Capacidad de Habitacion para Niños')
    room_price = models.IntegerField(verbose_name='Precio Habitacion',default=0)
    room_promo = models.IntegerField(verbose_name='Precio Promocional Habitacion',default=0)
    room_avaib = models.IntegerField(verbose_name='Cantidad de Habitaciones disponibles',default=1)
    room_avaib_use = models.IntegerField(verbose_name='Cantidad de Habitaciones Usadas', default=0)
    room_services = models.ManyToManyField(ServiceRoom,related_name='service_name_room')
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True,blank=True)

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'

    def __str__(self):
        return self.room_hotel.hotel_lugar.name_place + ' '+ self.room_name

    def get_room_services(self):
        return "\n".join([p.service_name for p in self.room_services.all()])


class PhotosRoom(models.Model):
    room_hotel_ph = models.ForeignKey(Rooms,on_delete=models.DO_NOTHING)
    photo_room = models.ImageField(upload_to='room/photos/',null=True)

    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True,blank=True)

    class Meta:
        verbose_name = 'Foto de Habitacion'
        verbose_name_plural = 'Fotos de Habitaciones'

    def __str__(self):
        return self.room_hotel_ph.room_hotel.hotel_lugar.name_place + ' ' + self.room_hotel_ph.room_name + ' ' + str(self.photo_room)