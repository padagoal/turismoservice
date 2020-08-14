from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.


class Departamento(models.Model):
    numero_dpto = models.IntegerField(default=0,verbose_name='Numero de Departamento')
    nombre_dpto = models.CharField(max_length=255,verbose_name='Nombre de Departamento')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ('numero_dpto',)

    def __str__(self):
        return self.nombre_dpto


class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=255,verbose_name='Nombre de la Ciudad')
    dpto_ciudad = models.ForeignKey(Departamento,on_delete=models.CASCADE,verbose_name='Departamento')
    descripcion_ciudad = models.TextField(max_length=500,verbose_name='Descripcion de Ciudad',default='',
                                          blank=True,null=True)
    position = GeopositionField(null=True,blank=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ('nombre_ciudad',)

    def __str__(self):
        return self.nombre_ciudad


class LugarTipo(models.Model):
    place_type = models.CharField(max_length=100,default='',verbose_name='Tipo de Lugar')
    active = models.BooleanField(default='True',verbose_name='Activo')
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True,blank=True)

    class Meta:
        verbose_name = 'Tipo de Lugar'
        verbose_name_plural = 'Tipos de Lugares'
        ordering = ('place_type',)

    def __str__(self):
        return self.place_type


class ViajeTipo(models.Model):
    travel_type = models.CharField(max_length=100,default='Tipo de Viaje')
    active = models.BooleanField(default='True', verbose_name='Activo')
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True,blank=True)

    class Meta:
        verbose_name = 'Tipo de Viaje'
        verbose_name_plural = 'Tipos de Viajes'
        ordering = ('travel_type',)

    def __str__(self):
        return self.travel_type


class DestinoTipo(models.Model):
    destiny_type = models.CharField(max_length=100, default='Tipo de Destino')
    active = models.BooleanField(default='True', verbose_name='Activo')
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True,blank=True)

    class Meta:
        verbose_name = 'Tipo de Destino'
        verbose_name_plural = 'Tipos de Destinos'
        ordering = ('destiny_type',)

    def __str__(self):
        return self.destiny_type


class ActividadesTipo(models.Model):
    activities_type = models.CharField(max_length=100,default='Tipo de Actividades')
    active = models.BooleanField(default='True', verbose_name='Activo')
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    created_by = models.CharField(verbose_name='created_by', default='', max_length=200, null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now_add=True, null=True)
    updated_by = models.CharField(verbose_name='updated_by', default='', max_length=200, null=True,blank=True)

    class Meta:
        verbose_name = 'Tipo de Actividad'
        verbose_name_plural = 'Tipos de Actividades'
        ordering = ('activities_type',)

    def __str__(self):
        return self.activities_type


class Lugar(models.Model):
    name_place = models.CharField(max_length=255,verbose_name='Nombre del Lugar')
    description_place = models.TextField(max_length=1000,verbose_name='Descripcion del Lugar')
    ciudad_lugar = models.ForeignKey(Ciudad,verbose_name='Ciudad',on_delete=models.DO_NOTHING,null=True,default=None)
    lat_pos = models.CharField(max_length=255,verbose_name='Latitud Posicion',null=True)
    long_pos = models.CharField(max_length=255,verbose_name='Longitud Posicion',null=True)
    direccionlugar = models.CharField(max_length=500,verbose_name='Direccion Lugar',null=True,blank=True)
    telefonolugar = models.CharField(max_length=255,verbose_name='Contacto Lugar',null=True,blank=True)
    whatsapp_place = models.CharField(max_length=255,verbose_name='Whatsapp',null=True,blank=True)
    facebook_profile = models.CharField(max_length=500,verbose_name='Perfil Facebook',null=True,blank=True)
    instagram_profile = models.CharField(max_length=500, verbose_name='Instagram Facebook', null=True, blank=True)
    twitter_profile = models.CharField(max_length=500, verbose_name='Twitter Facebook', null=True, blank=True)
    website_lugar = models.CharField(max_length=500, verbose_name='Pagina web', null=True, blank=True)
    position_lugar = GeopositionField(null=True, blank=True)
    is_hotel = models.BooleanField(verbose_name='Es Hotel?',default=False)
    foto_lugar = models.ImageField(upload_to='lugar/',null=True)
    tipo_lugar = models.ManyToManyField(LugarTipo,related_name='lugar_tipo')
    tipo_viaje_lugar = models.ManyToManyField(ViajeTipo,related_name='viaje_tipo')
    tipo_destino_lugar = models.ManyToManyField(DestinoTipo,related_name='destino_tipo')
    tipo_actividad_lugar = models.ManyToManyField(ActividadesTipo,related_name='actividad_tipo')

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        ordering = ('name_place',)

    def __str__(self):
        return self.name_place

    def get_tipo_lugar(self):
        return "\n".join([p.place_type for p in self.tipo_lugar.all()])

    get_tipo_lugar.short_description = 'Tipo de Lugar'

    def get_tipo_viaje_lugar(self):
        return "\n".join([p.travel_type for p in self.tipo_viaje_lugar.all()])

    get_tipo_viaje_lugar.short_description = 'Tipo de Viaje'

    def get_tipo_destino_lugar(self):
        return "\n".join([p.destiny_type for p in self.tipo_destino_lugar.all()])

    get_tipo_destino_lugar.short_description = 'Tipo de Destino'

    def get_tipo_actividad_lugar(self):
        return "\n".join([p.activities_type for p in self.tipo_actividad_lugar.all()])

    get_tipo_actividad_lugar.short_description = 'Tipo de Actividad'

