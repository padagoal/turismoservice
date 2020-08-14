from rest_framework import serializers
from TurismoPlace.models import LugarTipo,DestinoTipo,ActividadesTipo,ViajeTipo


class LugarTipoSerial(serializers.ModelSerializer):

    class Meta:
        model = LugarTipo
        fields = ('place_type',)



