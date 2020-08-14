from django.contrib import admin
from TurismoPlace.models import *
# Register your models here.


admin.site.register(LugarTipo)
admin.site.register(ViajeTipo)
admin.site.register(DestinoTipo)
admin.site.register(ActividadesTipo)


class LugarAdmin(admin.ModelAdmin):
    list_display = (('name_place'),('is_hotel'),('ciudad_lugar'),('get_tipo_lugar'),('get_tipo_viaje_lugar'),
                    ('get_tipo_destino_lugar'),('get_tipo_actividad_lugar'),)
    search_fields = (('name_place'),('ciudad_lugar'),('get_tipo_lugar'),('get_tipo_viaje_lugar'),
                    ('get_tipo_destino_lugar'),('get_tipo_actividad_lugar'),)


admin.site.register(Lugar,LugarAdmin)


admin.site.register(Departamento)
admin.site.register(Ciudad)

