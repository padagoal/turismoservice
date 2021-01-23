from django.urls import path
from TurismoPlace.views import *
from TurismoTour.views import *
from TurismoBlog.views import *
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
    path('singleplacetourinfo/<int:pk>',tour_info,name='singleplacetourinfo'),
    path('deletetour/<int:pk>',delete_tour,name='deletetour'),
    path('singleplacetourinfo/',tour_info,name='singleplacetourinfo'),

    path('listAvailableRooms/',listAvailableRoomsVista,name= 'listAvailableRooms'),

    path('createReservation/<int:pk>',createReservation,name='createReservation'),

    path('enviarMail/',enviarMail,name='enviarMail'),


    #CustomTour
    path('customtour/',customtour,name='customtour'),

    path('showUserTour/',list_tour_user,name='showUserTour'),

    path('listPlacesForTour/',listPlacesForTour,name='listPlacesForTour'),

    path('drawPlacesForTour/',draw_list_places_user_choice,name='drawPlacesForTour'),

    path('saveTourFromUser/',saveTourFromUser,name='saveTourFromUser'),





    #Blog

    path('blog/index/',index_blog,name='indexBlog'),
    path('blog/newPost/',post_new,name='newPost'),
    path('blog/login/',login_user_blog,name='blogLogin'),
    path('blog/logout/',logout_user_blog,name='blogLogout'),
    path('blog/PostUser',post_user,name='postUser')

]

#?ciudad=4&actividad=8#