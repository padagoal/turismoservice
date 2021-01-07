from django.urls import path
from TurismoPlace.views import *
from TurismoTour.views import *
urlpatterns = [

    #API
    #path('admin/', admin.site.urls),
    path('lugartipofiltro/',lugartipofiltro,name ='lugartipofiltro'),
    path('destinotipofiltro/',destinotipofiltro,name='destinotipofiltro'),
    path('viajetipofiltro/',viajetipofiltro,name='viajetipofiltro'),
    path('actividadtipofiltro/',actividadtipofiltro,name='actividadtipofiltro'),
    path('ciudadfiltro/',ciudadfiltro,name='ciudadfiltro'),
    path('lugarAll/',lugarAll,name='lugarAll'),

    path('buscarActividad/',buscarActividad,name= 'buscarActividad'),



    #Vistas
    path('buscarActividadVista/',buscarActividadVista,name= 'buscarActividadVista'),
    path('buscarViajeVista/',buscarViajeVista,name= 'buscarViajeVista'),
    path('buscarDestinoVista/',buscarDestinoVista,name='buscarDestinoVista'),
    path('buscarLugarVista/',buscarLugarVista,name='buscarLugarVista'),

    path('singleplaceinfo/',singleplaceinfo,name= 'singleplaceinfo'),
    path('singleplacehotelinfo/',singleplacehotelinfo,name= 'singleplacehotelinfo'),
    path('singleplacetourinfo/',tour_info,name='singleplacetourinfo'),




    #CustomTour
    path('customtour/',customtour,name='customtour'),

    path('listPlacesForTour/',listPlacesForTour,name='listPlacesForTour')


]

#?ciudad=4&actividad=8#