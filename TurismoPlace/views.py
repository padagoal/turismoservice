from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import date
from .serializers import LugarTipoSerial, DestinoTipoSerial, ActividadTipoSerial, ViajeTipoSerial, CiudadFiltroSerial, \
    LugarSerial, LugarSerialAll
from TurismoPlace.models import LugarTipo, DestinoTipo, ActividadesTipo, ViajeTipo, Ciudad, Lugar
from TurismoHotel.models import Hotel, Rooms, PhotosHotel, ReservasHotel
from django.http import HttpResponse, JsonResponse
from TurismoHotel.forms import ReservaHotelForm
from utils import send_mail

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

    return JsonResponse(serializer.data, safe=False, status=200)


def listAvailableRoomsVista(request):
    if request.GET.get('ciudad') is not None:
        ciudad = request.GET.get('ciudad')
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=ciudad)
        nombre_ciudad = Ciudad.objects.get(pk=ciudad)
    else:
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=3)
        nombre_ciudad = Ciudad.objects.get(pk=3)
        ciudad = 1

    checkin = ""
    rango_original = ""
    if request.GET.get('checkin') is not None and request.GET.get('checkin') is not '':
        checkin = request.GET.get('checkin')
        rango_original = checkin
        checkin = checkin.strip(" ")

    adults = 1
    if request.GET.get('adults') is not None and request.GET.get('adults') is not '':
        adults = int(request.GET.get('adults'))
    children = 0
    if request.GET.get('children') is not None and request.GET.get('adults') is not '':
        children = int(request.GET.get('children'))

    fechasSeparadas = checkin.split("-")
    fechaCheckin = fechasSeparadas[0].split("/")
    fechaCheckout = fechasSeparadas[1].split("/")

    fechaCheckinDato = fechaCheckin[2].strip(" ") + "-" + fechaCheckin[1].strip(" ") + "-" + fechaCheckin[0].strip(" ")
    fechaCheckoutDato = fechaCheckout[2].strip(" ") + "-" + fechaCheckout[1].strip(" ") + "-" \
                        + fechaCheckout[0].strip(" ")

    #habitaciones_por_ciudad = Rooms.objects.filter(room_hotel__hotel_lugar__ciudad_lugar_id=ciudad,
    #                                               room_capacity_adult__gte=adults,
    #                                               room_capacity_child__gte=children)

    reservas_en_fecha_pedida = ReservasHotel.objects.filter(
        rooms_selected__room_hotel__hotel_lugar__ciudad_lugar_id=ciudad,
        fecha_inicio_reservada__gte=fechaCheckinDato,
        fecha_fin_reservada__lte=fechaCheckoutDato)

    habitaciones_libres = Rooms.objects.filter(room_hotel__hotel_lugar__ciudad_lugar_id=ciudad,
                                               room_capacity_adult__gte=adults,
                                               room_capacity_child__gte=children) \
        .exclude(pk__in=obtener_pk_habitaciones(reservas_en_fecha_pedida))\


    return render(request, 'travelix/listlugar_rooms.html', {
        'titulo': 'Hoteles en ' + nombre_ciudad.nombre_ciudad,
        'lista_data': habitaciones_libres,
        'nombre_ciudad': nombre_ciudad.nombre_ciudad,
        'activar': 'hotel',
        'rango_original':rango_original,
        'rango_buscardor':fechaCheckinDato+"/"+fechaCheckoutDato,
        'cantidad_people':adults
    })



def obtener_pk_habitaciones(reservas_en_fecha_pedida):
    listPk = []
    for reservas in reservas_en_fecha_pedida:
        listPk.append(reservas.rooms_selected.pk)

    return listPk


@login_required(login_url='/login')
def createReservation(request,pk):

    rango_fecha = request.GET.get('rangofec')
    cantidad_personas_reserva = request.GET.get('cantidad_people')
    rango_fecha_sep = rango_fecha.split("/")
    checkIn = rango_fecha_sep[0].split("-")
    checkOut = rango_fecha_sep[1].split("-")
    habitacion_a_reservar = Rooms.objects.get(pk=pk)
    user_id = request.user.id
    fecha_reserva = date.today()

    f_date = date(int(checkIn[0]), int(checkIn[1]), int(checkIn[2]))
    l_date = date(int(checkOut[0]), int(checkOut[1]), int(checkOut[2]))
    cantidad_dias_reserva = int((l_date - f_date).days)

    if habitacion_a_reservar.room_promo > 0:
        costo_reserva = habitacion_a_reservar.room_promo * cantidad_dias_reserva
    else:
        costo_reserva = habitacion_a_reservar.room_price*cantidad_dias_reserva

    formReservaHotel = ReservaHotelForm()

    reserva = formReservaHotel.save(commit=False)

    reserva.rooms_selected=habitacion_a_reservar
    reserva.fecha_reserva = fecha_reserva
    reserva.fecha_inicio_reservada = f_date
    reserva.fecha_fin_reservada = l_date
    reserva.cantidad_dias_reserva = cantidad_dias_reserva
    reserva.cantidad_personas_reserva = cantidad_personas_reserva
    reserva.user_id = user_id
    reserva.costo_reserva = costo_reserva

    reserva.save()

    send_mail.enviar_mail()

    return render(request, 'travelix/reserva/overview_reserva_hotel.html', {
        'reserva': reserva,
        'rangofecha ': rango_fecha,
        'costo_reserva': costo_reserva
    })



def buscarActividadVista(request):
    if request.GET.get('ciudad') is not None:
        ciudad = request.GET.get('ciudad')
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=ciudad)
        nombre_ciudad = Ciudad.objects.get(pk=ciudad)
    else:
        lista_dato = Lugar.objects.filter(ciudad_lugar__id=3)
        nombre_ciudad = Ciudad.objects.get(pk=3)

    if request.GET.get('actividad') is not None and request.GET.get('actividad') is not '':
        actividad = request.GET.get('actividad')
        lista_dato = lista_dato.filter(tipo_actividad_lugar=actividad)

    if request.is_ajax():
        return render(request, 'travelix/onlylistlugar.html', {
            'titulo': 'Teste',
            'lista_data': lista_dato,
            'nombre_ciudad': nombre_ciudad.nombre_ciudad,
            'activar': 'actividad'
        })
    else:
        return render(request, 'travelix/listlugar.html', {
            'titulo': 'Atractivos en ' + nombre_ciudad.nombre_ciudad,
            'lista_data': lista_dato,
            'nombre_ciudad': nombre_ciudad.nombre_ciudad,
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
            'nombre_ciudad': nombre_ciudad.nombre_ciudad,
            'activar': 'viaje'
        })
    else:
        return render(request, 'travelix/listlugar.html', {
            'titulo': 'Atractivos en ' + nombre_ciudad.nombre_ciudad,
            'lista_data': lista_dato,
            'nombre_ciudad': nombre_ciudad.nombre_ciudad,
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
            'nombre_ciudad': nombre_ciudad.nombre_ciudad,
            'activar': 'lugar'
        })
    else:
        return render(request, 'travelix/listlugar.html', {
            'titulo': 'Atractivos en ' + nombre_ciudad.nombre_ciudad,
            'lista_data': lista_dato,
            'nombre_ciudad': nombre_ciudad.nombre_ciudad,
            'activar': 'lugar'
        })


def buscarDestinoVista(request):
    # if request.GET.get('ciudad') is not None:
    #    ciudad = request.GET.get('ciudad')
    #    lista_dato = Lugar.objects.filter(ciudad_lugar__id=ciudad)
    #    nombre_ciudad = Ciudad.objects.get(pk=ciudad)
    # else:
    #    lista_dato = Lugar.objects.filter(ciudad_lugar__id=3)
    #    nombre_ciudad = Ciudad.objects.get(pk=3)
    nombre_destino = ''
    # lista_dato = Lugar.objects.all()
    if request.GET.get('destino') is not None and request.GET.get('destino') is not '':
        destino = request.GET.get('destino')
        lista_dato = Lugar.objects.filter(tipo_destino_lugar=destino)
        nombre_destino = DestinoTipo.objects.get(pk=destino)

    if request.is_ajax():
        return render(request, 'travelix/onlylistlugar.html', {
            'titulo': 'Teste',
            'lista_data': lista_dato,
            'nombre_ciudad': nombre_destino.destiny_type,
            'activar': 'destino'
        })
    else:
        return render(request, 'travelix/listlugar.html', {
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
            'lugar': lugar
        })


def singleplacehotelinfo(request):
    lugar_a_buscar = request.GET.get('lugar')
    if lugar_a_buscar is not None and lugar_a_buscar is not '':
        lugar = Lugar.objects.get(pk=lugar_a_buscar)
        hotel = Hotel.objects.get(hotel_lugar=lugar)
        rooms = Rooms.objects.filter(room_hotel=hotel)
        photo_hotel = PhotosHotel.objects.filter(hotel_ph=hotel)
        return render(request, 'travelix/single_listing_hotel.html', {
            'lugar': lugar,
            'hotel': hotel,
            'rooms': rooms,
            'photo_hotel': photo_hotel,

        })


def lugartipofiltro(request):
    lut = LugarTipo.objects.filter(active=True)
    serializer = LugarTipoSerial(lut, many=False)
    return JsonResponse(serializer.data, safe=False, status=200)


def destinotipofiltro(request):
    lista = DestinoTipo.objects.filter(active=True)
    serializer = DestinoTipoSerial(lista, many=False)
    return JsonResponse(serializer.data, safe=False, status=200)


def actividadtipofiltro(request):
    lista = ActividadesTipo.objects.filter(active=True)
    serializer = ActividadTipoSerial(lista, many=False)
    return JsonResponse(serializer.data, safe=False, status=200)


def viajetipofiltro(request):
    lista = ViajeTipo.objects.filter(active=True)
    serializer = ViajeTipoSerial(lista, many=False)
    return JsonResponse(serializer.data, safe=False, status=200)


def ciudadfiltro(request):
    lista = Ciudad.objects.all()
    serializer = CiudadFiltroSerial(lista, many=False)
    return JsonResponse(serializer.data, safe=False, status=200)


def lugarAll(request):
    lista = Lugar.objects.all()
    serializer = LugarSerialAll(lista, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)
