from rest_framework import serializers
from TurismoPlace.models import LugarTipo,DestinoTipo,ActividadesTipo,ViajeTipo,Ciudad,Lugar


class LugarTipoSerial(serializers.Serializer):
    datos = serializers.SerializerMethodField('get_place_type')

    def get_place_type(self, obj):
        try:
            query = LugarTipo.objects.all()
            if query:
                data = list(query.values('id', 'place_type'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def create(self, validated_data):
        return LugarTipo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        """

        return instance


class DestinoTipoSerial(serializers.Serializer):
    datos = serializers.SerializerMethodField('get_destiny_type')

    def get_destiny_type(self, obj):
        try:
            query = DestinoTipo.objects.all()
            if query:
                data = list(query.values('id', 'destiny_type'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def create(self, validated_data):
        return DestinoTipo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        """

        return instance


class ActividadTipoSerial(serializers.Serializer):
    datos = serializers.SerializerMethodField('get_activities_type')

    def get_activities_type(self, obj):
        try:
            query = ActividadesTipo.objects.all()
            if query:
                data = list(query.values('pk', 'activities_type'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def create(self, validated_data):
        return ActividadesTipo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        """

        return instance


class ViajeTipoSerial(serializers.Serializer):
    datos = serializers.SerializerMethodField('get_viaje_tipo')

    def get_viaje_tipo(self, obj):
        try:
            query = ViajeTipo.objects.all()
            if query:
                data = list(query.values('id', 'travel_type'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def create(self, validated_data):
        return ViajeTipo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        """

        return instance


class CiudadSerial(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('nombre_ciudad','dpto_ciudad','descripcion_ciudad','position')


class LugarSerial(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ('name_place','description_place','foto_lugar','get_tipo_lugar','tipo_viaje_lugar',)


class CiudadFiltroSerial(serializers.Serializer):
    datos = serializers.SerializerMethodField('get_id_ciudad')

    def get_id_ciudad(self,obj):
        try:
            query = Ciudad.objects.all()
            if query:
                data = list(query.values('id','nombre_ciudad'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def create(self, validated_data):
        return Ciudad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        """

        return instance