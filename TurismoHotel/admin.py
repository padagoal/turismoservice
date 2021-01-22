from django.contrib import admin
from TurismoHotel.models import *
# Register your models here.


admin.site.register(ServiceHotel)
admin.site.register(ServiceRoom)


class PhotosHotelInline(admin.TabularInline):
    model = PhotosHotel


class HotelAdmin(admin.ModelAdmin):
    list_display = (('hotel_lugar'), ('get_hotel_ciudad'),('get_hotel_services'),)
    inlines = [
        PhotosHotelInline,
    ]


admin.site.register(Rooms)
admin.site.register(Hotel,HotelAdmin)
