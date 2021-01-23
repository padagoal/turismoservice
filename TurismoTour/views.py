from random import randint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from TurismoPlace.models import ActividadesTipo, LugarTipo, ViajeTipo, Lugar
from itertools import chain
from .forms import *
from sequences import get_next_value


# Create your views here.


def tour_info(request, pk):
    tour_a_buscar = pk
    if request.GET.get('tour'):
        tour_a_buscar = request.GET.get('tour')

    if tour_a_buscar is not None and tour_a_buscar is not '':
        tour = Tour.objects.get(pk=tour_a_buscar)
    else:
        tour = Tour.objects.get(pk=1)
    return render(request, 'travelix/single_listing_tour.html', {
        'tour': tour,
    })


def delete_tour(request, pk):
    tour_a_eliminar = pk
    tour_delete = Tour.objects.get(pk=tour_a_eliminar)
    if tour_delete:
        tour_delete.delete()
    else:
        return redirect(list_tour_user)
    return redirect(list_tour_user)


def _get_random_tour():
    services = Tour.objects.filter(is_from_staff=True)
    i = randint(0, services.count() - 1)
    return services[i]


def list_tour_user(request):
    tours = Tour.objects.filter(user_id=request.user.id)
    data_staff = _get_random_tour()
    mensaje_vacio = False
    if len(tours) > 0:
        mensaje_vacio = True

    if not mensaje_vacio:
        response = {
            'data_staff': data_staff,
            'mensaje_vacio': mensaje_vacio
        }
    else:
        response = {
            'lista_data': tours,
            'data_staff': data_staff,
            'mensaje_vacio': mensaje_vacio
        }

    return render(request, 'travelix/itinerario/showUserTour.html', response)


@login_required(login_url='/login')
def customtour(request):
    listactividades = ActividadesTipo.objects.all().filter(active=True)
    listlugartipo = LugarTipo.objects.all().filter(active=True)
    listaviaje = ViajeTipo.objects.all().filter(active=True)
    return render(request, 'travelix/customTourCreate.html',
                  {'listactividades': listactividades,
                   'listlugartipo': listlugartipo,
                   'listaviaje': listaviaje})


def draw_list_places_user_choice(request):
    places = request.GET.get('places')
    lugares = Lugar.objects.filter(pk__in=places.split(","))
    return render(request, 'travelix/itinerario/listPlacesUserChoice.html', {'lugares': lugares})


def listPlacesForTour(request):
    ciudad_a_buscar = request.GET.get('citysearch')
    listViaje = request.GET.get('listviaje')
    listLugar = request.GET.get('listlugar')
    listActi = request.GET.get('listacti')

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
    if result_list_limpia:
        lista_resultado = result_list_limpia
    else:
        lista_resultado = listLugaresAmostrar_

    return render(request, 'travelix/onlylistlugar_tour.html',
                  {'lista_data': lista_resultado, })


@login_required(login_url='/login')
def saveTourFromUser(request):
    user = request.user
    tour_name = request.POST.get('tourName')
    list_places = request.POST.get("listPlaces")

    tourPlaces = Lugar.objects.filter(pk__in=list_places.split(","))

    formTour = TourForm()

    tour = formTour.save(commit=False)

    tour.id = get_next_value("tours")
    tour.tour_name = tour_name
    tour.tour_short_descripcion = 'Tour creado por ' + user.username
    tour.tour_description = 'Tour creado por ' + user.username

    tour.tour_photo_cover = 'itinerario/image.jpeg'
    tour.tour_cost = 0
    tour.is_from_user = True
    tour.is_from_staff = False
    tour.tour_active = True
    tour.user_id = request.user.id

    tour.save()
    tour.tour_lugar.set(tourPlaces)
    tour.save()

    return list_tour_user(request)
