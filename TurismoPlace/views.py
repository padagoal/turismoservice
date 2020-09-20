from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .serializers import LugarTipoSerial,DestinoTipoSerial,ActividadTipoSerial,ViajeTipoSerial,CiudadFiltroSerial,LugarSerial
from TurismoPlace.models import LugarTipo,DestinoTipo,ActividadesTipo,ViajeTipo,Ciudad,Lugar
from TurismoHotel.models import Hotel,Rooms,PhotosHotel
from django.http import HttpResponse, JsonResponse
# Create your views here.


def buscarActividad(request):
    if request.GET.get('ciudad') is not None:
        ciudad = request.GET.get('ciudad')
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=ciudad)
    else:
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=3)

    if request.GET.get('actividad') is not None:
        actividad = request.GET.get('actividad')
        lista_dato = lista_dato.filter(tipo_actividad_lugar=actividad)

    serializer = LugarSerial(lista_dato, many=True)

    return JsonResponse(serializer.data,safe=False,status=200)


def buscarActividadVista(request):
    if request.GET.get('ciudad') is not None:
        ciudad = request.GET.get('ciudad')
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=ciudad)
        nombre_ciudad = Ciudad.objects.get(pk=ciudad)
    else:
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=3)
        nombre_ciudad = Ciudad.objects.get(pk=3)

    if request.GET.get('actividad') is not None and request.GET.get('actividad') is not '' :
        actividad = request.GET.get('actividad')
        lista_dato = lista_dato.filter(tipo_actividad_lugar=actividad)

    if request.is_ajax():
        return render(request, 'travelix/onlylistlugar.html', {
            'titulo': 'Teste',
            'lista_data': lista_dato,
            'nombre_ciudad':  nombre_ciudad.nombre_ciudad,
            'activar': 'actividad'
        })
    else:
        return render(request,'travelix/listlugar.html',{
            'titulo': 'Atractivos en ' + nombre_ciudad.nombre_ciudad,
            'lista_data': lista_dato,
            'nombre_ciudad':  nombre_ciudad.nombre_ciudad,
            'activar': 'actividad'
        })


def buscarViajeVista(request):
    if request.GET.get('ciudad') is not None:
        ciudad = request.GET.get('ciudad')
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=ciudad)
        nombre_ciudad = Ciudad.objects.get(pk=ciudad)
    else:
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=3)
        nombre_ciudad = Ciudad.objects.get(pk=3)

    if request.GET.get('viaje') is not None and request.GET.get('viaje') is not '':
        viaje = request.GET.get('viaje')
        lista_dato = lista_dato.filter(tipo_viaje_lugar=viaje)

    if request.is_ajax():
        return render(request, 'travelix/onlylistlugar.html', {
            'titulo': 'Teste',
            'lista_data': lista_dato,
            'nombre_ciudad':  nombre_ciudad.nombre_ciudad,
            'activar':'viaje'
        })
    else:
        return render(request,'travelix/listlugar.html',{
            'titulo': 'Atractivos en ' + nombre_ciudad.nombre_ciudad,
            'lista_data': lista_dato,
            'nombre_ciudad':  nombre_ciudad.nombre_ciudad,
            'activar': 'viaje'
        })

def buscarLugarVista(request):
    if request.GET.get('ciudad') is not None:
        ciudad = request.GET.get('ciudad')
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=ciudad)
        nombre_ciudad = Ciudad.objects.get(pk=ciudad)
    else:
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=3)
        nombre_ciudad = Ciudad.objects.get(pk=3)

    if request.GET.get('lugar') is not None and request.GET.get('lugar') is not '':
        lugar = request.GET.get('lugar')
        lista_dato = lista_dato.filter(tipo_lugar=lugar)

    if request.is_ajax():
        return render(request, 'travelix/onlylistlugar.html', {
            'titulo': 'Teste',
            'lista_data': lista_dato,
            'nombre_ciudad':  nombre_ciudad.nombre_ciudad,
            'activar':'lugar'
        })
    else:
        return render(request,'travelix/listlugar.html',{
            'titulo': 'Atractivos en ' + nombre_ciudad.nombre_ciudad,
            'lista_data': lista_dato,
            'nombre_ciudad':  nombre_ciudad.nombre_ciudad,
            'activar': 'lugar'
        })


def buscarDestinoVista(request):
    #if request.GET.get('ciudad') is not None:
    #    ciudad = request.GET.get('ciudad')
    #    lista_dato = Lugar.objects.filter(ciudad_lugar__id=ciudad)
    #    nombre_ciudad = Ciudad.objects.get(pk=ciudad)
    #else:
    #    lista_dato = Lugar.objects.filter(ciudad_lugar__id=3)
    #    nombre_ciudad = Ciudad.objects.get(pk=3)
    nombre_destino = ''
    #lista_dato = Lugar.objects.all()
    if request.GET.get('destino') is not None and request.GET.get('destino') is not '':
        destino = request.GET.get('destino')
        lista_dato = Lugar.objects.filter(tipo_destino_lugar=destino)
        nombre_destino = DestinoTipo.objects.get(pk=destino)

    if request.is_ajax():
        return render(request, 'travelix/onlylistlugar.html', {
            'titulo': 'Teste',
            'lista_data': lista_dato,
            'nombre_ciudad': nombre_destino.destiny_type,
            'activar':'destino'
        })
    else:
        return render(request,'travelix/listlugar.html',{
            'titulo': 'Atractivos en ' + nombre_destino.destiny_type,
            'lista_data': lista_dato,
            'nombre_ciudad': nombre_destino.destiny_type,
            'activar': 'destino'
        })




def singleplaceinfo(request):
    lugar_a_buscar = request.GET.get('lugar')
    if lugar_a_buscar is not None and lugar_a_buscar is not '':
        lugar = Lugar.objects.get(pk=lugar_a_buscar)
        return render(request, 'travelix/single_listing.html', {
            'lugar':lugar
        })


def singleplacehotelinfo(request):
    lugar_a_buscar = request.GET.get('lugar')
    if lugar_a_buscar is not None and lugar_a_buscar is not '':
        lugar = Lugar.objects.get(pk=lugar_a_buscar)
        hotel = Hotel.objects.get(hotel_lugar=lugar)
        rooms = Rooms.objects.filter(room_hotel=hotel)
        photo_hotel = PhotosHotel.objects.filter(hotel_ph=hotel)
        return render(request, 'travelix/single_listing_hotel.html', {
            'lugar':lugar,
            'hotel':hotel,
            'rooms':rooms,
            'photo_hotel': photo_hotel,

        })



def lugartipofiltro(request):
    lut = LugarTipo.objects.filter(active=True)
    serializer = LugarTipoSerial(lut,many=False)
    return JsonResponse(serializer.data,safe=False, status=200)


def destinotipofiltro(request):
    lista = DestinoTipo.objects.filter(active=True)
    serializer = DestinoTipoSerial(lista,many=False)
    return JsonResponse(serializer.data,safe=False, status=200)


def actividadtipofiltro(request):
    lista = ActividadesTipo.objects.filter(active=True)
    serializer = ActividadTipoSerial(lista,many=False)
    return JsonResponse(serializer.data,safe=False, status=200)


def viajetipofiltro(request):
    lista = ViajeTipo.objects.filter(active=True)
    serializer = ViajeTipoSerial(lista,many=False)
    return JsonResponse(serializer.data,safe=False, status=200)


def ciudadfiltro(request):
    lista = Ciudad.objects.all()
    serializer = CiudadFiltroSerial(lista,many=False)
    return JsonResponse(serializer.data,safe=False, status=200)