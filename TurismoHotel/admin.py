from django.contrib import admin
from TurismoHotel.models import *
# Register your models here.


admin.site.register(ServiceHotel)
admin.site.register(ServiceRoom)


admin.site.register(Hotel)
#admin.site.register(Rooms)

class PhotosRoomInline(admin.TabularInline):
    model = PhotosRoom

admin.site.register(PhotosRoom)

class RoomAdmin(admin.ModelAdmin):
    inlines = [
        PhotosRoomInline,
    ]

admin.site.register(Rooms,RoomAdmin)
