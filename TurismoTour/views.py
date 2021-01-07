from django.shortcuts import render
from .models import Tour
from TurismoPlace.models import ActividadesTipo, LugarTipo, ViajeTipo, Lugar
from itertools import chain



# Create your views here.


def tour_info(request):
    tour_a_buscar = request.GET.get('tour')
    if tour_a_buscar is not None and tour_a_buscar is not '':
        tour = Tour.objects.get(pk=tour_a_buscar)
    else:
        tour = Tour.objects.get(pk=1)
    return render(request, 'travelix/single_listing_tour.html', {
        'tour': tour,
    })


def customtour(request):
    listactividades = ActividadesTipo.objects.all().filter(active=True)
    listlugartipo = LugarTipo.objects.all().filter(active=True)
    listaviaje = ViajeTipo.objects.all().filter(active=True)
    return render(request, 'travelix/customTourCreate.html',
                  {'listactividades': listactividades,
                   'listlugartipo': listlugartipo,
                   'listaviaje': listaviaje})


def listPlacesForTour(request):
    ciudad_a_buscar = request.GET.get('citysearch')
    listViaje = request.GET.get('listviaje')
    listLugar = request.GET.get('listlugar')
    listActi = request.GET.get('listacti')

    print(ciudad_a_buscar)

    lugar_filtro_list = []
    viaje_filtro_list = []
    acti_filtro_list = []

    listLugaresAmostrar_ = Lugar.objects.filter(ciudad_lugar=ciudad_a_buscar)

    if listLugar:
        lugar_filtro_list = listLugaresAmostrar_.filter(tipo_lugar__in=listLugar.split(","))
    if listViaje:
        viaje_filtro_list = listLugaresAmostrar_.filter(tipo_viaje_lugar__in=listViaje.split(","))
    if listActi:
        acti_filtro_list = listLugaresAmostrar_.filter(tipo_actividad_lugar__in=listActi.split(","))

    result_list = list(chain(lugar_filtro_list, viaje_filtro_list, acti_filtro_list))
    result_list_limpia = list(dict.fromkeys(result_list))

    print(result_list_limpia)

    return render(request, 'travelix/onlylistlugar_tour.html',
                  {'lista_data': result_list_limpia,})