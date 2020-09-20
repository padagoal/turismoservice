from django.contrib import admin
from TurismoHotel.models import *
# Register your models here.


admin.site.register(ServiceHotel)
admin.site.register(ServiceRoom)



class PhotosHotelInline(admin.TabularInline):
    model = PhotosHotel



class HotelAdmin(admin.ModelAdmin):
    inlines = [
        PhotosHotelInline,
    ]


admin.site.register(Rooms)
admin.site.register(Hotel,HotelAdmin)
